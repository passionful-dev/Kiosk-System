from django.contrib import admin
from .models import User, User_type, Supplier, Received_item, Sold_item, Item_batch, Item_properties, Item, Category

# Register your models here.
@admin.register(User_type)
class User_typeAdmin(admin.ModelAdmin):
    #pass
    # list_display = ('user,')
    readonly_fields = ('timestamp',)
#admin.site.register(User_type)

admin.site.register(User)
admin.site.register(Supplier)
admin.site.register(Received_item)
admin.site.register(Sold_item)
admin.site.register(Item_batch)
admin.site.register(Item_properties)
admin.site.register(Item)
admin.site.register(Category)
