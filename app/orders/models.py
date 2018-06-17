from django.db import models


class Order(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='order_id')
    customer = models.ForeignKey('users.Customer', models.DO_NOTHING, db_column='customer_id', blank=True, null=True)
    employee = models.ForeignKey('users.Employee', models.DO_NOTHING, db_column='employee_id', blank=True, null=True)
    order_date = models.DateField(db_column='order_date', blank=True, null=True)
    required_date = models.DateField(db_column='require_ddate', blank=True, null=True)
    shipped_date = models.DateField(db_column='shipped_date', blank=True, null=True)
    ship_via = models.ForeignKey('users.Shipper', models.DO_NOTHING, db_column='shipvia', blank=True, null=True)
    freight = models.FloatField(blank=True, null=True)

    ship_name = models.CharField(db_column='ship_name', max_length=40, blank=True, null=True)
    ship_address = models.CharField(db_column='ship_address', max_length=60, blank=True, null=True)
    ship_city = models.CharField(db_column='ship_city', max_length=15, blank=True, null=True)
    ship_region = models.CharField(db_column='ship_region', max_length=15, blank=True, null=True)
    ship_postalcode = models.CharField(db_column='ship_postalcode', max_length=10, blank=True, null=True)
    ship_country = models.CharField(db_column='ship_country', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class OrderDetail(models.Model):
    id = models.OneToOneField(Order, models.DO_NOTHING, db_column='order_id', primary_key=True)
    product = models.OneToOneField('products.Product', models.DO_NOTHING, db_column='product_id')
    unit_price = models.FloatField(db_column='unit_price')
    quantity = models.SmallIntegerField(db_column='quantity')
    discount = models.FloatField(db_column='discount')

    class Meta:
        managed = False
        db_table = 'order_details'
