from django.contrib import admin
from django.contrib.auth import get_user_model

# Now register the new UserAdmin...
admin.site.register(get_user_model())

