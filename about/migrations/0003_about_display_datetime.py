"""Add display_datetime field.

Created to match the migration history already recorded in the database.
"""
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0002_alter_about_content"),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='display_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

