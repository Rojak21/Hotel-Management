from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import  Create_item, aboutus, dashboard, delete_item,index, menu,signin,signup, update_item

urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('aboutus/', aboutus, name='aboutus'),
    path('menu/', menu, name='menu'),
    path('Create_item/', Create_item, name='Create_item'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('update_item/<int:item_id>/', update_item, name='update_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
