# Generated by Django 3.0.3 on 2021-03-16 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210316_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatsapp',
            name='confirm_paid',
            field=models.BooleanField(default=False),
        ),
    ]