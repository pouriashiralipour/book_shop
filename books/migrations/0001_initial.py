# Generated by Django 4.2.3 on 2023-07-31 09:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('price', models.PositiveBigIntegerField()),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'ordering': ['-datetime_created'],
            },
        ),
    ]
