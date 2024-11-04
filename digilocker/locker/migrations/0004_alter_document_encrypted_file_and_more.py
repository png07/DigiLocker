# Generated by Django 5.1.2 on 2024-10-28 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0003_rename_key_document_encryption_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='encrypted_file',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='encryption_key',
            field=models.CharField(max_length=255),
        ),
    ]