# Generated by Django 2.2 on 2019-04-19 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20190419_0829'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='show',
            order_with_respect_to='theatre',
        ),
    ]
