# Generated by Django 4.2.2 on 2023-06-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0006_rename_age_appointment_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default='someone@example.com', max_length=254),
            preserve_default=False,
        ),
    ]
