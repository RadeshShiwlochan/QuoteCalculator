# Generated by Django 2.0.2 on 2018-03-30 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteCalculator', '0004_auto_20180330_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='administration',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='annualTotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='bathrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='bedrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='cap_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='insurance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='management',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='marketing',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='monthlyRent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='payroll',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='repairs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='taxes',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='unitNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='utility',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='vacancy',
            field=models.IntegerField(default=0),
        ),
    ]
