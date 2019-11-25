# Generated by Django 2.1 on 2019-05-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_weatherforcastmodel_locationname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weatherforcastmodel',
            options={'ordering': ['dateTime']},
        ),
        migrations.AddField(
            model_name='weatherforcastmodel',
            name='ingestion_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]