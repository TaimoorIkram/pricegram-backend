from django.contrib import admin

from restbase.models import Product, VisitHistory, SearchHistory, ViewHistory, Favourite


admin.site.register(Product)
admin.site.register(VisitHistory)
admin.site.register(SearchHistory)
admin.site.register(ViewHistory)
admin.site.register(Favourite)