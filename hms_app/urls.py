from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import  Create_item, aboutus, create_orders, dashboard,delete_item, delete_order,index, item_list, menu,signin,signup,update_item, update_order

urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('aboutus/', aboutus, name='aboutus'),
    path('menu/', menu, name='menu'),
    path('item_list/', item_list, name='item_list'),
    path('Create_item/', Create_item, name='Create_item'),
    path('delete_item/', delete_item, name='delete_item'),
    path('update_item/', update_item, name='update_item'),
    path('create_orders/', create_orders, name='create_orders'),
    path('update_order/', update_order, name='update_order'),
    path('delete_order/', delete_order, name='delete_order'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
