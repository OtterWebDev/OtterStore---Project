# Generated by Django 4.1.5 on 2023-02-07 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustomer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uservendor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_vendor', to=settings.AUTH_USER_MODEL),
        ),
    ]
