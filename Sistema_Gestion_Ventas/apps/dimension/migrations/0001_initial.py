# Generated by Django 2.2.5 on 2019-10-09 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidad_medida', '0001_initial'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id_dimension', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_dimension', models.CharField(max_length=45)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Producto')),
                ('id_unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidad_medida.Unidad_Medida')),
            ],
        ),
    ]
