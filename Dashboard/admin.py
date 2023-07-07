
# Register your models here.
from django.contrib import admin
from .models import *
from accounts.models import CustomUser

class PostAdmin(admin.ModelAdmin):
    list_display=['title','image','user','category','created','slug']


class NationAdmin(admin.ModelAdmin):
    list_display=['title','image','user','category','created','slug']

    # prepopulated_fields = {"slug": ("title")}
class AllianceAdmin(admin.ModelAdmin):
    list_display=['title','image','user','category','created','slug']

admin.site.register(Post,PostAdmin)
admin.site.register(CustomUser)





