# Generated by Django 2.2.2 on 2019-06-11 03:03

import colorfield.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='last name')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('short_name', models.CharField(max_length=60, null=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('twitter', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Twitter @username', regex='^@[A-Za-z0-9_]{1,15}$')], verbose_name='Twitter Handle')),
                ('website', models.URLField(blank=True, null=True)),
                ('website_display', models.CharField(blank=True, max_length=120, null=True)),
                ('brand_color', colorfield.fields.ColorField(blank=True, max_length=18, null=True)),
                ('google_analytics', models.BooleanField(default=False)),
                ('google_analytics_funcname', models.CharField(blank=True, max_length=128, null=True)),
                ('compact_player', models.BooleanField(default=False)),
                ('enterprise', models.BooleanField(default=False)),
                ('blogging_platforms', models.CharField(choices=[('W', 'Wordpress'), ('H', 'HTML'), ('M', 'Medium'), ('D', 'Drupal'), ('S', 'Squarespace'), ('O', 'Other')], help_text='Blogging Platform / CMS', max_length=1)),
                ('audio_hub', models.BooleanField(default=True, help_text='Audio Hub')),
                ('podcasts', models.BooleanField(default=False, help_text='Podcasts')),
                ('amazon_alexa', models.BooleanField(default=False, help_text='Amazon Alexa')),
                ('google_actions', models.BooleanField(default=False, help_text='Google Actions')),
                ('narrations_available', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('read_dt', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='user',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='users.Customer'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]