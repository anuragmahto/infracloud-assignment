# Generated by Django 5.1.4 on 2024-12-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0002_remove_urlstore_expired_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=50, unique=True)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
