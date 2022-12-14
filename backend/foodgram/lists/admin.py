from django.contrib import admin

from .models import Favorite, ShoppingList, Subscription


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')


admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingList)
admin.site.register(Subscription)
