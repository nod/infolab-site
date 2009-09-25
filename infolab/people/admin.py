from infolab.people.models import Person, Paper
from django.contrib import admin

admin.site.register(Paper)

class PersonAdmin(admin.ModelAdmin):
    fields = ( 'username', 'face', 'first_name',
               'last_name', 'title', 'grouping', 'email', 'is_staff',
               'twitter', 'website', 'office', 'telephone',
               'interests', 'descr', 'papers', )
    list_display = ('username', 'first_name', 'last_name', 'email', 'grouping')
admin.site.register(Person, PersonAdmin)
