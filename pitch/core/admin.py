from django.contrib import admin
from core.models import Pitch

@admin.register(Pitch)
class PitchAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller_name', 'product_name', 'submitted_at')  # Customize columns
    search_fields = ('seller_name', 'product_name')
    readonly_fields = ('ai_feedback',)
