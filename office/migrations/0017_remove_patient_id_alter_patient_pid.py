# Generated by Django 4.2.2 on 2023-06-30 06:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0016_rename_doc_type_appointment_doc_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AlterField(
            model_name='patient',
            name='pid',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
