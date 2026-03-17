from django import forms
from .models import Transaction, Category, Subcategory, TransactionType, Status

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'type': forms.Select(attrs={'class': 'form-select', 'id': 'id_type'}),
            'category': forms.Select(attrs={'class': 'form-select', 'id': 'id_category'}),
            'subcategory': forms.Select(attrs={'class': 'form-select', 'id': 'id_subcategory'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Категории теперь всегда доступны все
        self.fields['category'].queryset = Category.objects.all()
        
        if self.instance.pk and self.instance.subcategory:
            # При редактировании подгружаем подкатегории текущей категории
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category)
        else:
            # Иначе пусто, пока не выбрана категория
            self.fields['subcategory'].queryset = Subcategory.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')

        # Осталась только валидация: Подкатегория должна относиться к Категории
        if category and subcategory:
            if subcategory.category != category:
                raise forms.ValidationError("Выбранная подкатегория не относится к выбранной категории.")

        return cleaned_data

# Формы для справочников
class TypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'] # Убрали transaction_type из полей
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }