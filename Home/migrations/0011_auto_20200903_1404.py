# Generated by Django 3.1.1 on 2020-09-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_principal_color_interfaz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='color_interfaz',
            field=models.CharField(choices=[('/static/css/colors/green.css', 'Verde'), ('/static/css/colors/mossgreen.css', 'Verde Mostaza'), ('/static/css/colors/bridge.css', 'Verde Claro'), ('/static/css/colors/orange.css', 'Naranja'), ('/static/css/colors/pink.css', 'Rosado'), ('/static/css/colors/red.css', 'Rojo'), ('/static/css/colors/purple.css', 'Morado'), ('/static/css/colors/yellow.css', 'Amarillo'), ('/static/css/colors/violet.css', 'Violeta'), ('/static/css/colors/cyan.css', 'Cyan')], default='Verde', max_length=100),
        ),
    ]
