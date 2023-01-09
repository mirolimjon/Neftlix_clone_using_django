from django.contrib import admin
from .models import Profile, CustomUser, Movies, Video
# Register your models here.


admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(Movies)
admin.site.register(Video)