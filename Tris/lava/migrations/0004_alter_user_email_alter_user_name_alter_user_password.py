# Generated by Django 5.0.3 on 2024-03-22 16:35

import secured_fields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lava', '0003_rename_country_info_b_place_info_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=secured_fields.fields.EncryptedCharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=secured_fields.fields.EncryptedCharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=secured_fields.fields.EncryptedCharField(max_length=20),
        ),
    ]
