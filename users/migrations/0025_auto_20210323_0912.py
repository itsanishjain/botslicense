# Generated by Django 3.0.3 on 2021-03-23 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_profile_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Funy',
        ),
    ]
