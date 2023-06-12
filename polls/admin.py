from django.contrib import admin

# Register your models here.
from .models import Album, Portfolio, News

admin.site.register(Album)
admin.site.register(Portfolio)
admin.site.register(News)