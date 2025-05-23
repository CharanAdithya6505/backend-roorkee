# Generated by Django 4.2.20 on 2025-05-03 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communityEmpowerment', '0021_alter_faq_options_faq_order_faq_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPrivacySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_information_usage', models.BooleanField(default=False)),
                ('allow_information_sharing', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
