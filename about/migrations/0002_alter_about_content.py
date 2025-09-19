"""Split migration: alter content field to SummernoteTextField.

Created to match the migration history already recorded in the database.
"""
from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=django_summernote.fields.SummernoteTextField(blank=True),
        ),
    ]

# DELETED: This migration file has been removed by the developer and will be deleted.
