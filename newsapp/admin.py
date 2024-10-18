from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import *

# Register your models here.
admin.site.register(category)
# admin.site.register(news_detail)
admin.site.register(comment)
admin.site.unregister(Group)

@admin.register(news_detail)
class cupan_admin(admin.ModelAdmin):
    list_display=["newsheador","newsposition","newscetegory","date"]

admin.site.index_title="Galaxy News admin"
admin.site.site_header="Galaxy News admin"
admin.site.site_title="Galaxy News admin"

# admin.site.unregister(User)