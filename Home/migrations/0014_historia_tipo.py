# Generated by Django 3.1.1 on 2020-09-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_auto_20200904_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia',
            name='tipo',
            field=models.CharField(choices=[('Pasion', 'Pasión'), ('Historia', 'Historia')], default='Historia', max_length=30),
        ),
    ]
