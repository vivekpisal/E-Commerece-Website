from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base,name='base'),
    path('register',views.register,name='register'),
    path('products',views.products,name='products'),
    path('additems',views.additems,name='additems'),
    path('addtype',views.addtype,name='addtype'),
    path('showcart',views.showcart,name='showcart'),
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path('deleteitem/<int:id>',views.deleteitem,name='deleteitem'),
    path('oneorder/<int:id>',views.oneorder,name='oneorder'),
    path('category/<str:category>',views.category,name='category'),
    path('deletecart/<str:name>',views.deletecart,name='deletecart'),
    path('allorder',views.allorder,name='allorder'),
    path('showproduct/<int:id>',views.showproduct,name='showproduct'),
]



if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)