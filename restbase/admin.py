from django.contrib import admin

from restbase.models import Product, VisitHistory, SearchHistory, ViewHistory, Favourite, Like, Review, SiteFeedback, BugStatus


admin.site.register(Product)
admin.site.register(VisitHistory)
admin.site.register(SearchHistory)
admin.site.register(ViewHistory)
admin.site.register(Favourite)
admin.site.register(Like)
admin.site.register(Review)
admin.site.register(BugStatus)
admin.site.register(SiteFeedback)