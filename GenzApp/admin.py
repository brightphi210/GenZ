from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Authors)
admin.site.register(AuthorsProfile)
admin.site.register(Category)
admin.site.register(NewsLetter)
admin.site.register(News)
admin.site.register(Stories)
admin.site.register(SubscriptionPlan)