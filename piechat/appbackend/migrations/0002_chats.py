# Generated by Django 2.2.7 on 2019-11-09 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('receiver', models.CharField(max_length=30)),
                ('sent', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
