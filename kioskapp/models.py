from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class User_type(models.Model):
    timestamp = models.DateTimeField(default = timezone.now(), editable=False)
    # Make permission class instead
    # PERMISSIONS = (
    #     ('0', 'No access'),
    #     ('1', 'Read'),
    #     ('2', 'Read/Write/Update'),
    #     ('3', 'All access'),
    # )
    # permission = models.ModelMul.CharField(
    #     max_length=1, 
    #     choices=PERMISSIONS,
    #     default='0',
    #     help_text='Select user permission',
    # )
    user_type_name = models.CharField(max_length=15, help_text='Enter user type')

    class Meta:
        verbose_name_plural = "User types"
    
    def __str__(self):
        return self.user_type_name
    
    def get_absolute_url(self):
        return reverse('user_type-detail', args=[str(self.id)])

class User(models.Model):
    timestamp = models.DateTimeField(default = timezone.now(), editable=False)
    fullname = models.CharField('Full name', max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    #raw_password = models.CharField(max_length=50)
    #password = make_password(raw_password)
    mobile = models.CharField(max_length=15)
    user_type = models.ManyToManyField(User_type, help_text='Select user type')

    def __str__(self):
        return self.fullname
    
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

class Category(models.Model):
    timestamp = models.DateTimeField(default = timezone.now(), editable=False)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    category_name = models.CharField(max_length=15, help_text='Enter category name')
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

class Item(models.Model):
    #timestamp = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(default=timezone.now(), editable=False)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    barcode = models.CharField('Bar code', max_length=10, help_text='Enter barcode')
    item_name = models.CharField(max_length=25, help_text='Enter item name')
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True, help_text='Select category')
    brandname = models.CharField('Brand name', max_length=25, help_text='Enter brand name')
    modelname = models.CharField('Model name', max_length=25, help_text='Enter model name')
    item_description = models.TextField(max_length=50, help_text='Enter item description')
    # item_batch_info = models.ForeignKey('Item_batch', on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, help_text='Select supplier')
    sellingprice = models.FloatField('Selling price', help_text='Enter selling price')

    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

class Item_properties(models.Model):
    # Vare_egenskaber_id = models.AutoField(primary_key = True)
    timestamp = models.DateTimeField(default = timezone.now(), editable=False)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete = models.SET_NULL, null=True, help_text='Select item')
    color = models.CharField(max_length = 25, help_text='Enter item color')
    size = models.CharField(max_length = 20, help_text='Enter item size')
    weight = models.FloatField(help_text='Enter item weight')

    class Meta:
        verbose_name_plural = "Item properties"

    def __str__(self):
        return self.color

    def get_absolute_url(self):
        return reverse('item_properties-detail', args=[str(self.id)])
 

class Item_batch(models.Model):
    # Vare_batch_id = models.AutoField(primary_key = True)
    timestamp = models.DateTimeField(default = timezone.now(), editable=False)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete = models.SET_NULL, null=True, help_text='Select item')
    item_batch_code = models.CharField(max_length = 15, help_text='Enter batch code')
    manufacture_date = models.DateField(help_text='Enter manufacture date')
    expiry_date = models.DateField(help_text='Enter expiry date')
    
    class Meta:
        verbose_name_plural = "Item batches"

    def __str__(self):
        return self.item_batch_code
    
    def get_absolute_url(self):
        return reverse('item_batch-detail', args=[str(self.id)])

class Supplier(models.Model):
    # supplier_id = models.AutoField(primary_key = True)
    timestamp = models.DateTimeField(default = timezone.now(), editable=False)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    #item_info = models.ForeignKey(Item, on_delete = models.SET_NULL, null=True)
    supplier_name = models.CharField(max_length = 40, help_text='Enter supplier name')
    
    def __str__(self):
        return self.supplier_name
    
    def get_absolute_url(self):
        return reverse('supplier-detail', args=[str(self.id)])

class Received_item(models.Model):
    # modtaget_id = models.AutoField(primary_key = True)
    timestamp = models.DateTimeField(default = timezone.now(), editable=False)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete = models.SET_NULL, null=True, help_text='Select item')
    received_quantity = models.IntegerField(help_text='Enter received quantity')
    cost_price = models.FloatField(help_text='Enter cost price')
    price_per_piece = models.FloatField(help_text='Enter price of single piece')

    class Meta:
        verbose_name_plural = "Received items"

    def __str__(self):
        # return f'{self.received_quantity} ({self.item.item_name})'
        return f'{self.item.item_name}'
    
    def get_absolute_url(self):
        return reverse('received_item-detail', args=[str(self.id)])

class Sold_item(models.Model):
    # solgt_id = models.AutoField(primary_key = True)
    timestamp = models.DateTimeField(default = timezone.now(), editable=False)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete = models.CASCADE, help_text='Select item')
    #item = models.ForeignKey(Item, on_delete = models.SET_NULL, null=True, help_text='Select item')
    sold_quantity = models.IntegerField(help_text='Enter sold quantity')

    class Meta:
        verbose_name_plural = "Sold items"

    def __str__(self):
        return f'{self.item.item_name}'
    
    def get_absolute_url(self):
        return reverse('sold_item-detail', args=[str(self.id)])

