# Generated by Django 2.2 on 2019-05-03 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0009_auto_20190419_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('row_num', models.PositiveSmallIntegerField()),
                ('col_num', models.PositiveSmallIntegerField()),
                ('status', models.IntegerField(choices=[(1, 'AVAILABLE'), (2, 'BLOCKED'), (3, 'BOOKED')], default=1)),
                ('session', models.CharField(max_length=200)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_show', to='dashboard.show')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('show', 'row_num', 'col_num')},
            },
        ),
    ]
