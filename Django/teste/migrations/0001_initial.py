# Generated by Django 5.1.1 on 2024-10-07 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBase',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('modelbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teste.modelbase')),
                ('name', models.CharField(db_column='tx_name', max_length=100, null=True)),
                ('age', models.IntegerField(db_column='tx_age', null=True)),
                ('rg', models.CharField(max_length=100)),
            ],
            bases=('teste.modelbase',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('modelbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teste.modelbase')),
                ('name', models.CharField(max_length=100)),
                ('registraction', models.CharField(max_length=100)),
            ],
            bases=('teste.modelbase',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('modelbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teste.modelbase')),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
            bases=('teste.modelbase',),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('modelbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teste.modelbase')),
                ('nrf', models.CharField(max_length=100)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teste.cliente')),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teste.employee')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teste.product')),
            ],
            bases=('teste.modelbase',),
        ),
    ]
