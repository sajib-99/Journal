from django.contrib import admin

from .models import Contact
from .models import Editor_Request
from .models import Reviewer_Request
from .models import Submitted_Paper

from .models import UserProfile
# Register your models here.

admin.site.register(Contact)
admin.site.register(Editor_Request)
admin.site.register(Reviewer_Request)
admin.site.register(Submitted_Paper)

class UserProfileAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'Email', 'FirstName', 'LastName', 'Subscription')
    list_editable = ( 'Email', 'FirstName', 'LastName', 'Subscription')

admin.site.register(UserProfile, UserProfileAdmin)