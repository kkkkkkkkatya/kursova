# Generated by Django 4.2.7 on 2023-11-29 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.directors'),
        ),
        migrations.AlterField(
            model_name='films',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Рік'),
        ),
    ]