from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Transaction, Category, Subcategory, TransactionType, Status
from .forms import TransactionForm, TypeForm, StatusForm, CategoryForm, SubcategoryForm

def index(request):
    transactions = Transaction.objects.all().select_related('type', 'category', 'subcategory', 'status').order_by('-date')
    
    # Фильтры
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    type_id = request.GET.get('type')
    status_id = request.GET.get('status')
    category_id = request.GET.get('category')

    if date_from:
        transactions = transactions.filter(date__gte=date_from)
    if date_to:
        transactions = transactions.filter(date__lte=date_to)
    if type_id:
        transactions = transactions.filter(type_id=type_id)
    if status_id:
        transactions = transactions.filter(status_id=status_id)
    if category_id:
        transactions = transactions.filter(category_id=category_id)

    context = {
        'transactions': transactions,
        'types': TransactionType.objects.all(),
        'statuses': Status.objects.all(),
        'categories': Category.objects.all(),
        'selected_type': type_id,
        'selected_status': status_id,
        'selected_category': category_id,
        'date_from': date_from,
        'date_to': date_to,
    }
    return render(request, 'transactions/index.html', context)

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно создана!')
            return redirect('index')
    else:
        form = TransactionForm()
    return render(request, 'transactions/form.html', {'form': form, 'title': 'Новая транзакция'})

def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись обновлена!')
            return redirect('index')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/form.html', {'form': form, 'title': 'Редактирование транзакции', 'object': transaction})

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        messages.warning(request, 'Запись удалена.')
        return redirect('index')
    return render(request, 'transactions/delete.html', {'object': transaction})

# Управление справочниками
def manage_dictionary(request, model_name, pk=None):
    models_map = {
        'types': (TransactionType, TypeForm, 'Типы операций'),
        'statuses': (Status, StatusForm, 'Статусы'),
        'categories': (Category, CategoryForm, 'Категории'),
        'subcategories': (Subcategory, SubcategoryForm, 'Подкатегории'),
    }
    
    if model_name not in models_map:
        return redirect('index')
        
    model, form_class, title = models_map[model_name]
    
    if pk: 
        obj = get_object_or_404(model, pk=pk)
        if request.method == 'POST':
            if 'delete' in request.POST:
                obj.delete()
                messages.success(request, f'{title[:-1]} удален.')
                return redirect('manage_dictionary', model_name=model_name)
            form = form_class(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, f'{title[:-1]} обновлен.')
                return redirect('manage_dictionary', model_name=model_name)
        else:
            form = form_class(instance=obj)
        return render(request, 'transactions/dictionary_form.html', {'form': form, 'title': f'Редактировать: {title}', 'model_name': model_name})
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{title[:-1]} добавлен.')
            return redirect('manage_dictionary', model_name=model_name)
    else:
        form = form_class()
    
    items = model.objects.all().select_related('category') if model == Subcategory else model.objects.all()
    
    return render(request, 'transactions/dictionary_list.html', {
        'items': items,
        'form': form,
        'title': title,
        'model_name': model_name
    })

def ajax_load_categories(request):
    # Теперь просто возвращаем все категории, тип не нужен
    categories = Category.objects.all().order_by('name')
    data = list(categories.values('id', 'name'))
    return JsonResponse(data, safe=False)

def ajax_load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    data = list(subcategories.values('id', 'name'))
    return JsonResponse(data, safe=False)