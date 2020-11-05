from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # path('items/', views.item_list_view, name='items'),
    path('items/', views.ItemsListView.as_view(), name='items'),
    # path('item/<int:primary_key>', views.item_detail_view, name='item-detail'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('suppliers/', views.SuppliersListView.as_view(), name='suppliers'),
    path('supplier/<int:pk>', views.SupplierDetailView.as_view(), name='supplier-detail'),
    path('categories/', views.CategoriesListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('receiveditems/', views.ReceivedItemsListView.as_view(), name='receiveditems'),
    path('receiveditem/<int:pk>', views.ReceivedItemDetailView.as_view(), name='received_item-detail'),
    path('solditems/', views.SoldItemsListView.as_view(), name='solditems'),
    path('solditem/<int:pk>', views.SoldItemDetailView.as_view(), name='sold_item-detail'),
    # path('solditem/<int:pk>', views.sold_item_view, name='sold_item_detail'),
    
    path('item/create/', views.ItemCreate.as_view(), name='item_create'),
    path('item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
    path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
]