# Generated by Django 3.1.3 on 2020-11-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201112_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='orderItemId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]