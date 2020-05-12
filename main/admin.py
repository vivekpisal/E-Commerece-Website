from django.contrib import admin
from .models import *

from image_cropping import ImageCroppingMixin

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
# Register your models here.

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Type)
admin.site.register(Product,MyModelAdmin)