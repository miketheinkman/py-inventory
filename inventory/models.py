from django.db import models


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50)
    vendor_email = models.CharField(max_length=75)

    def __str__(self):
        return self.vendor_name


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=500)
    item_cost = models.DecimalField(max_digits=10, decimal_places=2)
    item_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(default=0)
    item_use_quantity = models.IntegerField(default=1)
    item_order_point = models.IntegerField(default=0)
    item_max_quantity = models.IntegerField(default=1)
    item_barcode = models.CharField(max_length=100)

    def __str__(self):
        return str(self.item_name) + " - " + str(self.item_vendor) + " - " + "QTY: " + str(self.item_quantity)


class Email(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    monday = models.BooleanField()
    monday_time = models.TimeField('Monday Time', blank=True)

    tuesday = models.BooleanField()
    tuesday_time = models.TimeField('Tuesday Time', blank=True)

    wednesday = models.BooleanField()
    wednesday_time = models.TimeField('Wednesday Time', blank=True)

    thursday = models.BooleanField()
    thursday_time = models.TimeField('Thursday Time', blank=True)

    friday = models.BooleanField()
    friday_time = models.TimeField('Friday Time', blank=True)

    saturday = models.BooleanField()
    saturday_time = models.TimeField('Saturday Time', blank=True)

    sunday = models.BooleanField()
    sunday_time = models.TimeField('Sunday Time', blank=True)

    def __str__(self):
        return str(self.vendor)


class ListItem(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item

