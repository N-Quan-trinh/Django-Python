from django.contrib import admin
from myWeb import models, forms

# Register your models here.
admin.site.register(models.Book)
admin.site.register(models.Game)
admin.site.register(models.Platform)
admin.site.register(models.UserAccount)



