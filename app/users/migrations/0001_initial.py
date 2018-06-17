# Generated by Django 2.0.6 on 2018-06-17 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(db_column='customerid', max_length=10, primary_key=True, serialize=False)),
                ('company_name', models.CharField(db_column='companyname', max_length=40)),
                ('contact_name', models.CharField(blank=True, db_column='contactname', max_length=30, null=True)),
                ('contact_title', models.CharField(blank=True, db_column='contacttitle', max_length=30, null=True)),
                ('address', models.CharField(blank=True, db_column='address', max_length=60, null=True)),
                ('city', models.CharField(blank=True, db_column='city', max_length=15, null=True)),
                ('region', models.CharField(blank=True, db_column='region', max_length=15, null=True)),
                ('postalcode', models.CharField(blank=True, db_column='postalcode', max_length=10, null=True)),
                ('country', models.CharField(blank=True, db_column='country', max_length=15, null=True)),
                ('phone', models.CharField(blank=True, db_column='phone', max_length=24, null=True)),
                ('fax', models.CharField(blank=True, db_column='fax', max_length=24, null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('id', models.CharField(db_column='customertypeid', max_length=10, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, db_column='customerdesc', null=True)),
            ],
            options={
                'db_table': 'customerdemographics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.SmallIntegerField(db_column='employeeid', primary_key=True, serialize=False)),
                ('last_name', models.CharField(db_column='lastname', max_length=20)),
                ('first_name', models.CharField(db_column='firstname', max_length=10)),
                ('title', models.CharField(blank=True, db_column='title', max_length=30, null=True)),
                ('title_of_courtesy', models.CharField(blank=True, db_column='titleofcourtesy', max_length=25, null=True)),
                ('birth_date', models.DateField(blank=True, db_column='birthdate', null=True)),
                ('hire_date', models.DateField(blank=True, db_column='hiredate', null=True)),
                ('address', models.CharField(blank=True, db_column='address', max_length=60, null=True)),
                ('city', models.CharField(blank=True, db_column='city', max_length=15, null=True)),
                ('region', models.CharField(blank=True, db_column='region', max_length=15, null=True)),
                ('postalcode', models.CharField(blank=True, db_column='postalcode', max_length=10, null=True)),
                ('country', models.CharField(blank=True, db_column='country', max_length=15, null=True)),
                ('homephone', models.CharField(blank=True, db_column='homephone', max_length=24, null=True)),
                ('extension', models.CharField(blank=True, db_column='extension', max_length=4, null=True)),
                ('photo', models.BinaryField(blank=True, db_column='photo', null=True)),
                ('notes', models.TextField(blank=True, db_column='notes', null=True)),
                ('photo_path', models.CharField(blank=True, db_column='photopath', max_length=255, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.SmallIntegerField(db_column='regionid', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='regiondescription', max_length=200)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.SmallIntegerField(db_column='shipperid', primary_key=True, serialize=False)),
                ('company_name', models.CharField(db_column='companyname', max_length=40)),
                ('phone', models.CharField(blank=True, db_column='phone', max_length=24, null=True)),
            ],
            options={
                'db_table': 'shippers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.CharField(db_column='territoryid', max_length=20, primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='territorydescription', max_length=200)),
            ],
            options={
                'db_table': 'territories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerDemo',
            fields=[
                ('id', models.OneToOneField(db_column='customerid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.Customer')),
            ],
            options={
                'db_table': 'customercustomerdemo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeTerritory',
            fields=[
                ('id', models.OneToOneField(db_column='employeeid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.Employee')),
            ],
            options={
                'db_table': 'employeeterritories',
                'managed': False,
            },
        ),
    ]