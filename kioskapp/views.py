from django.shortcuts import get_object_or_404, render
from .models import User, User_type, Supplier, Received_item, Sold_item, Item_batch, Item_properties, Item, Category
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# @login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some objects
    # num_items, num_categories, num_suppliers, num_receiveditems,
    # num_solditems, num_availableitems  
    num_items = Item.objects.all().count()
    num_categories = Category.objects.all().count()
    num_suppliers = Supplier.objects.all().count()
    num_receiveditems = Received_item.objects.all().count()
    # all() is implied by default
    num_solditems = Sold_item.objects.count()

    # Available items (change this. make it according to item name)
    num_availableitems = num_receiveditems - num_solditems

    context = {
        'num_items': num_items,
        'num_categories': num_categories,
        'num_suppliers': num_suppliers,
        'num_receiveditems': num_receiveditems,
        'num_solditems': num_solditems, 
        'num_availableitems': num_availableitems
    }

    # return render(request, 'index.html')
    return render(request, 'index.html', context=context)

class ItemsListView(generic.ListView):
    model = Item
    #allow_empty = False

class ItemDetailView(generic.DetailView):
    model = Item

# def item_list_view(request):
#     item = Item.objects.all()
#     return render(request, 'kioskapp/item_list.html', context={'item': item})

# def item_detail_view(request, primary_key):
#     item = get_object_or_404(Item, pk=primary_key)
#     return render(request, 'item_detail.html', context={'item': item})

class SuppliersListView(LoginRequiredMixin, generic.ListView):
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    model = Supplier

class SupplierDetailView(LoginRequiredMixin, generic.DetailView):
    model = Supplier

class CategoriesListView(generic.ListView):
    model = Category

class CategoryDetailView(generic.DetailView):
    model = Category

class ReceivedItemsListView(LoginRequiredMixin, generic.ListView):
    model = Received_item

class ReceivedItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Received_item

class SoldItemsListView(LoginRequiredMixin, generic.ListView):
    model = Sold_item

class SoldItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Sold_item

class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = '__all__'

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['barcode', 'item_name', 'category', 'brandname', 'modelname', 'item_description', 'supplier', 'sellingprice']

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('items')
    

