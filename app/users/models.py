from django.db import models


class Region(models.Model):
    id = models.SmallIntegerField(db_column='region_id', primary_key=True)
    description = models.CharField(db_column='region_description', max_length=200)

    class Meta:
        managed = False
        db_table = 'region'

    def __str__(self):
        return self.description


class Territory(models.Model):
    id = models.CharField(db_column='territory_id', primary_key=True, max_length=20)
    description = models.CharField(db_column='territory_description', max_length=200)
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='region_id')

    class Meta:
        managed = False
        db_table = 'territories'

    def __str__(self):
        return self.description


class EmployeeTerritory(models.Model):
    id = models.OneToOneField('Employee', models.DO_NOTHING, db_column='employee_id', primary_key=True)
    territory = models.OneToOneField(Territory, models.DO_NOTHING, db_column='territory_id')

    class Meta:
        managed = False
        db_table = 'employee_territories'


class Employee(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='employee_id')
    last_name = models.CharField(max_length=20, db_column='last_name')
    first_name = models.CharField(max_length=10, db_column='first_name')
    title = models.CharField(max_length=30, blank=True, null=True, db_column='title')
    title_of_courtesy = models.CharField(max_length=25, blank=True, null=True, db_column='title_of_courtesy')
    birth_date = models.DateField(blank=True, null=True, db_column='birth_date')
    hire_date = models.DateField(blank=True, null=True, db_column='hire_date')
    address = models.CharField(max_length=60, blank=True, null=True, db_column='address')
    city = models.CharField(max_length=15, blank=True, null=True, db_column='city')
    region = models.CharField(max_length=15, blank=True, null=True, db_column='region')
    postalcode = models.CharField(max_length=10, blank=True, null=True, db_column='postal_code')
    country = models.CharField(max_length=15, blank=True, null=True, db_column='country')
    homephone = models.CharField(max_length=24, blank=True, null=True, db_column='home_phone')
    extension = models.CharField(max_length=4, blank=True, null=True, db_column='extension')
    photo = models.BinaryField(blank=True, null=True, db_column='photo')
    notes = models.TextField(blank=True, null=True, db_column='notes')
    reports_to = models.ForeignKey('self', models.DO_NOTHING, db_column='reports_to', blank=True, null=True)
    photo_path = models.CharField(max_length=255, blank=True, null=True, db_column='photo_path')

    class Meta:
        managed = False
        db_table = 'employees'


class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=10, db_column='customer_id')
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

    class Meta:
        managed = False
        db_table = 'customers'

    def __str__(self):
        return self.company_name


class CustomerDemo(models.Model):
    id = models.OneToOneField(Customer, models.DO_NOTHING, db_column='customer_id', primary_key=True)
    customer_type = models.OneToOneField('CustomerType', models.DO_NOTHING, db_column='customer_type_id')

    class Meta:
        managed = False
        db_table = 'customer_customer_demo'


class CustomerType(models.Model):
    id = models.CharField(primary_key=True, max_length=10, db_column='customer_type_id')
    description = models.TextField(blank=True, null=True, db_column='customer_desc')

    class Meta:
        managed = False
        db_table = 'customer_demographics'

    def __str__(self):
        return self.description


class Shipper(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='shipper_id')
    company_name = models.CharField(max_length=40, db_column='company_name')
    phone = models.CharField(max_length=24, blank=True, null=True, db_column='phone')

    class Meta:
        managed = False
        db_table = 'shippers'

    def __str__(self):
        return self.company_name
