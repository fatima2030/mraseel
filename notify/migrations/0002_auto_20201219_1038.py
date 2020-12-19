# Generated by Django 3.1.3 on 2020-12-19 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notify', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noti_from_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noti_to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
