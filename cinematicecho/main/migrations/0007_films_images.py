# Generated by Django 4.2.7 on 2023-12-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_relfilmsactors'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='images',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
