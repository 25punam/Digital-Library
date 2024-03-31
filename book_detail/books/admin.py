from django.contrib import admin
from .models import BookModel, PageModel, ImageModel

# Register your models here.
admin.site.register(BookModel)
admin.site.register(PageModel)
admin.site.register(ImageModel)
