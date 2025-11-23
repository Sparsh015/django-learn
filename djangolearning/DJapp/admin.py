from django.contrib import admin
from .models import Varity, AnimeReview, Store, AnimeCertificate

# Register your models here.
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


admin.site.register(Varity)
