from django.contrib import admin
from.models import Member

class MemberAdmin(admin.ModelAdmin):
     list_display = ("firstname", "lastname", "phone","joined_date")

admin.site.register(Member, MemberAdmin)
