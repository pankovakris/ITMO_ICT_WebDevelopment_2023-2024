# Generated by Django 4.2.6 on 2023-10-31 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0006_remove_carowner_birth_date_remove_carowner_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carowner',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carowner',
            name='nationality',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='carowner',
            name='passport',
            field=models.CharField(max_length=50),
        ),
    ]
