# Generated by Django 5.1.6 on 2025-02-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_trackinghistory_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackinghistory',
            name='amount',
            field=models.FloatField(),
        ),
    ]
