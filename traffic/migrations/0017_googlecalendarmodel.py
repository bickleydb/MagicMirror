# Generated by Django 2.1.4 on 2018-12-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0016_auto_20181016_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleCalendarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_name', models.CharField(max_length=200)),
                ('calendar_id', models.CharField(max_length=500)),
            ],
        ),
    ]