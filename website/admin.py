from django.contrib import admin
from website.models import contact

# Register your models here.
#class ContactAdmin(admin.ModelAdmin):
#    date_hierarchy = ('created_date', )
#    list_display = ('name', 'email', 'created_date',) 
#    list_filter = ('name', 'email', )
#    search_fields = ('name', 'email', 'message')

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date') 
    list_filter = ('email',)
    search_fields = ('name', 'email', 'massage')

admin.site.register(contact, ContactAdmin)