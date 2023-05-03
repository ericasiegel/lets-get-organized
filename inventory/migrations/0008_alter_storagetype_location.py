# Generated by Django 4.2 on 2023-05-03 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0007_alter_object_category_alter_object_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storagetype",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="storage_type",
                to="inventory.location",
            ),
        ),
    ]
