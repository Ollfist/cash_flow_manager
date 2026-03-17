from django.contrib import admin
from .models import Transaction, TransactionType, Status, Category, Subcategory
# Register your models here.

admin.site.register(Transaction)
admin.site.register(TransactionType)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Subcategory)