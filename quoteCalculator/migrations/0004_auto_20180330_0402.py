# Generated by Django 2.0.2 on 2018-03-30 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteCalculator', '0003_auto_20180330_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='administration',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='annualTotal',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='bathrooms',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='bedrooms',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='cap_rate',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='insurance',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='management',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='marketing',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='monthlyRent',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='payroll',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='repairs',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='taxes',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='unitNumber',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='utility',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quote',
            name='vacancy',
            field=models.CharField(max_length=200),
        ),
    ]