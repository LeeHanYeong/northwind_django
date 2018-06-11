# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Product(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='productid')
    name = models.CharField(max_length=40, db_column='productname')
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='supplierid', blank=True, null=True)
    category = models.ForeignKey('Category', models.DO_NOTHING, db_column='categoryid', blank=True, null=True)
    quantity_per_unit = models.CharField(max_length=20, blank=True, null=True, db_column='quantityperunit')
    unit_price = models.FloatField(blank=True, null=True, db_column='unitprice')
    units_in_stock = models.SmallIntegerField(blank=True, null=True, db_column='unitsinstock')
    units_on_order = models.SmallIntegerField(blank=True, null=True, db_column='unitsonorder')
    reorder_level = models.SmallIntegerField(blank=True, null=True, db_column='reorderlevel')
    discontinued = models.IntegerField(db_column='discontinued')

    class Meta:
        managed = False
        db_table = 'products'


class Supplier(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='supplierid')
    company_name = models.CharField(max_length=40, db_column='companyname')
    contact_name = models.CharField(max_length=30, blank=True, null=True, db_column='contactname')
    contact_title = models.CharField(max_length=30, blank=True, null=True, db_column='contacttitle')
    address = models.CharField(max_length=60, blank=True, null=True, db_column='address')
    city = models.CharField(max_length=15, blank=True, null=True, db_column='city')
    region = models.CharField(max_length=15, blank=True, null=True, db_column='region')
    postalcode = models.CharField(max_length=10, blank=True, null=True, db_column='postalcode')
    country = models.CharField(max_length=15, blank=True, null=True, db_column='country')
    phone = models.CharField(max_length=24, blank=True, null=True, db_column='phone')
    fax = models.CharField(max_length=24, blank=True, null=True, db_column='fax')
    homepage = models.TextField(blank=True, null=True, db_column='homepage')

    class Meta:
        managed = False
        db_table = 'suppliers'


class Category(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='categoryid')
    name = models.CharField(max_length=15, db_column='categoryname')
    description = models.TextField(blank=True, null=True, db_column='description')
    picture = models.BinaryField(blank=True, null=True, db_column='picture')

    class Meta:
        managed = False
        db_table = 'categories'
