# Generated by Django 2.2.5 on 2019-10-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad_Medida',
            fields=[
                ('id_unidad_medida', models.AutoField(primary_key=True, serialize=False)),
                ('nom_unidad', models.CharField(max_length=45)),
                ('abreviatura', models.CharField(max_length=10)),
            ],
        ),
    ]
