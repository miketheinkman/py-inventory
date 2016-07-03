from django.contrib import admin
from .models import Item, Vendor, Email, ListItem

admin.site.register([Item, Vendor, Email, ListItem],)
