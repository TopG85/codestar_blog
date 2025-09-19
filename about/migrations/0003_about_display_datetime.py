"""Add display_datetime field.

Created to match the migration history already recorded in the database.
"""
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0002_about_display_datetime_alter_about_content"),
    ]

    # No operations: this migration was previously used to add `display_datetime` but
    # the field is already present (merged migration history). Keeping a no-op
    # preserves the migration numbering while preventing duplicate column creation
    # when running tests or creating a test database.
    operations = []

