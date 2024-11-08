# Generated by Django 5.1.2 on 2024-10-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0004_alter_document_encrypted_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_extension',
            field=models.CharField(default='.txt', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='encrypted_file',
            field=models.FileField(upload_to='media/encrypted_documents/'),
        ),
    ]
