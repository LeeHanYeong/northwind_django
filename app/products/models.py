from django.db import models


class Product(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='product_id')
    name = models.CharField(max_length=40, db_column='product_name')
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='supplier_id', blank=True, null=True)
    category = models.ForeignKey('Category', models.DO_NOTHING, db_column='category_id', blank=True, null=True)
    quantity_per_unit = models.CharField(max_length=20, blank=True, null=True, db_column='quantity_per_unit')
    unit_price = models.FloatField(blank=True, null=True, db_column='unit_price')
    units_in_stock = models.SmallIntegerField(blank=True, null=True, db_column='units_in_stock')
    units_on_order = models.SmallIntegerField(blank=True, null=True, db_column='units_on_order')
    reorder_level = models.SmallIntegerField(blank=True, null=True, db_column='reorder_level')
    discontinued = models.IntegerField(db_column='discontinued')

    class Meta:
        managed = False
        db_table = 'products'

    def __str__(self):
        return self.name


class Supplier(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='supplier_id')
    company_name = models.CharField(max_length=40, db_column='company_name')
    contact_name = models.CharField(max_length=30, blank=True, null=True, db_column='contact_name')
    contact_title = models.CharField(max_length=30, blank=True, null=True, db_column='contact_title')
    address = models.CharField(max_length=60, blank=True, null=True, db_column='address')
    city = models.CharField(max_length=15, blank=True, null=True, db_column='city')
    region = models.CharField(max_length=15, blank=True, null=True, db_column='region')
    postalcode = models.CharField(max_length=10, blank=True, null=True, db_column='postal_code')
    country = models.CharField(max_length=15, blank=True, null=True, db_column='country')
    phone = models.CharField(max_length=24, blank=True, null=True, db_column='phone')
    fax = models.CharField(max_length=24, blank=True, null=True, db_column='fax')
    homepage = models.TextField(blank=True, null=True, db_column='homepage')

    class Meta:
        managed = False
        db_table = 'suppliers'

    def __str__(self):
        return self.company_name


class Category(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='category_id')
    name = models.CharField(max_length=15, db_column='category_name')
    description = models.TextField(blank=True, null=True, db_column='description')
    picture = models.BinaryField(blank=True, null=True, db_column='picture')

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.name
