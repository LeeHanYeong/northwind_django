# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Order(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='orderid')
    customer = models.ForeignKey('Customer', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    order_date = models.DateField(db_column='orderdate', blank=True, null=True)
    required_date = models.DateField(db_column='requireddate', blank=True, null=True)
    shipped_date = models.DateField(db_column='shippeddate', blank=True, null=True)
    ship_via = models.ForeignKey('Shipper', models.DO_NOTHING, db_column='shipvia', blank=True, null=True)
    freight = models.FloatField(blank=True, null=True)

    ship_name = models.CharField(db_column='shipname', max_length=40, blank=True, null=True)
    ship_address = models.CharField(db_column='shipaddress', max_length=60, blank=True, null=True)
    ship_city = models.CharField(db_column='shipcity', max_length=15, blank=True, null=True)
    ship_region = models.CharField(db_column='shipregion', max_length=15, blank=True, null=True)
    ship_postalcode = models.CharField(db_column='shippostalcode', max_length=10, blank=True, null=True)
    ship_country = models.CharField(db_column='shipcountry', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class OrderDetail(models.Model):
    id = models.ForeignKey(Order, models.DO_NOTHING, db_column='orderid', primary_key=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='productid')
    unit_price = models.FloatField(db_column='unitprice')
    quantity = models.SmallIntegerField(db_column='quantity')
    discount = models.FloatField(db_column='discount')

    class Meta:
        managed = False
        db_table = 'order_details'
        unique_together = (
            ('id', 'product'),
        )
