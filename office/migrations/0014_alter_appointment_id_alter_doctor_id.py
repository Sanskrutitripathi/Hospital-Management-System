# Generated by Django 4.2.2 on 2023-06-27 10:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0013_alter_appointment_id_alter_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
