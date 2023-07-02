from django.contrib import admin

# Register your models here.
# admin 페이지에서 Post 뜨도록
from .models import Post

admin.site.register(Post)
