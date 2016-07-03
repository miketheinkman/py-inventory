from models import Item, Vendor, Email, ListItem

for a in Item.objects.all():
    print(a.item_name)