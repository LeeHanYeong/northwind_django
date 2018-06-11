# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Region(models.Model):
    id = models.SmallIntegerField(db_column='regionid', primary_key=True)
    description = models.CharField(db_column='regiondescription', max_length=200)

    class Meta:
        managed = False
        db_table = 'region'


class Territory(models.Model):
    id = models.CharField(db_column='territoryid', primary_key=True, max_length=20)
    description = models.CharField(db_column='territorydescription', max_length=200)
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='regionid')

    class Meta:
        managed = False
        db_table = 'territories'


class EmployeeTerritory(models.Model):
    id = models.ForeignKey('Employee', models.DO_NOTHING, db_column='employeeid', primary_key=True)
    territory = models.ForeignKey(Territory, models.DO_NOTHING, db_column='territoryid')

    class Meta:
        managed = False
        db_table = 'employeeterritories'
        unique_together = (
            ('id', 'territory'),
        )


class Employee(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='employeeid')
    last_name = models.CharField(max_length=20, db_column='lastname')
    first_name = models.CharField(max_length=10, db_column='firstname')
    title = models.CharField(max_length=30, blank=True, null=True, db_column='title')
    title_of_courtesy = models.CharField(max_length=25, blank=True, null=True, db_column='titleofcourtesy')
    birth_date = models.DateField(blank=True, null=True, db_column='birthdate')
    hire_date = models.DateField(blank=True, null=True, db_column='hiredate')
    address = models.CharField(max_length=60, blank=True, null=True, db_column='address')
    city = models.CharField(max_length=15, blank=True, null=True, db_column='city')
    region = models.CharField(max_length=15, blank=True, null=True, db_column='region')
    postalcode = models.CharField(max_length=10, blank=True, null=True, db_column='postalcode')
    country = models.CharField(max_length=15, blank=True, null=True, db_column='country')
    homephone = models.CharField(max_length=24, blank=True, null=True, db_column='homephone')
    extension = models.CharField(max_length=4, blank=True, null=True, db_column='extension')
    photo = models.BinaryField(blank=True, null=True, db_column='photo')
    notes = models.TextField(blank=True, null=True, db_column='notes')
    reports_to = models.ForeignKey('self', models.DO_NOTHING, db_column='reportsto', blank=True, null=True)
    photo_path = models.CharField(max_length=255, blank=True, null=True, db_column='photopath')

    class Meta:
        managed = False
        db_table = 'employee'


class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=-1, db_column='customerid')
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

    class Meta:
        managed = False
        db_table = 'customers'


class CustomerDemo(models.Model):
    id = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customerid', primary_key=True)
    customer_type = models.ForeignKey('CustomerType', models.DO_NOTHING, db_column='customertypeid')

    class Meta:
        managed = False
        db_table = 'customercustomerdemo'
        unique_together = (
            ('id', 'customer_type'),
        )


class CustomerType(models.Model):
    id = models.CharField(primary_key=True, max_length=10, db_column='customertypeid')
    description = models.TextField(blank=True, null=True, db_column='customerdesc')

    class Meta:
        managed = False
        db_table = 'customerdemographics'


class Shipper(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='shipperid')
    company_name = models.CharField(max_length=40, db_column='companyname')
    phone = models.CharField(max_length=24, blank=True, null=True, db_column='phone')

    class Meta:
        managed = False
        db_table = 'shippers'
