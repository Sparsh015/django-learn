from django.contrib import admin
from .models import Varity, AnimeReview, Store, AnimeCertificate

# Try unregistering to avoid AlreadyRegistered error
try:
    admin.site.unregister(Varity)
except admin.sites.NotRegistered:
    pass

class AnimeReviewInline(admin.TabularInline):
    model = AnimeReview
    extra = 2

class VarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [AnimeReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('anime_varieties',)

class AnimeCertificateAdmin(admin.ModelAdmin):
    list_display = ('anime', 'certificate_number')

admin.site.register(Varity, VarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(AnimeCertificate, AnimeCertificateAdmin)
