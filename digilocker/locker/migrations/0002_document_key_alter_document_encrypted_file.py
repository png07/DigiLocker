# Generated by Django 5.1.2 on 2024-10-28 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='key',
            field=models.BinaryField(default=b'12345678901234567890123456789012'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='encrypted_file',
            field=models.BinaryField(editable=True),
        ),
    ]