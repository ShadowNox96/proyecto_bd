# Generated by Django 2.2.5 on 2019-10-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]