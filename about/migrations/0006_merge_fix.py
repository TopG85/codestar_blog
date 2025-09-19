"""Merge migration to resolve divergent migration history for `about` app.

This is a no-op migration that depends on the two conflicting leaf nodes so
that Django's migration graph has a single tip. It avoids applying duplicate
schema changes during test DB creation.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_about_content'),
        ('about', '0005_collaboraterequest_remove_about_created_on_and_more'),
    ]

    operations = []
