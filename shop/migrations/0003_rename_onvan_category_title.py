# Generated by Django 4.1.1 on 2022-09-23 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_cp_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='onvan',
            new_name='title',
        ),
    ]