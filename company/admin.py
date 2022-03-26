from django.contrib import admin
from .models import SocialMedia

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'instagram', 'facebook', 'twitter', 'linkedin')
    list_display_links = ('email',)


admin.site.register(SocialMedia, SocialMediaAdmin)