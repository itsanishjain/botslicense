# Generated by Django 3.0.3 on 2021-03-22 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
        ('users', '0023_auto_20210322_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authtoken.Token'),
        ),
    ]
