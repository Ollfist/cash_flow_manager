from django.db import models

class TransactionType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name 

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    # Логическая зависимость: Подкатегория принадлежит Категории
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    
    def __str__(self):
        return f"{self.name} ({self.category})"

class Transaction(models.Model):
    date = models.DateField(verbose_name="Дата операции")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Статус")
    type = models.ForeignKey(TransactionType, on_delete=models.SET_NULL, null=True, verbose_name="Тип")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Подкатегория")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма (₽)")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.amount}₽ ({self.date})"