# Generated by Django 4.1 on 2022-09-05 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_selection"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="lat",
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="lng",
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
    ]
