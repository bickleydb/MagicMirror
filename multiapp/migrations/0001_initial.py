# Generated by Django 2.1 on 2018-11-25 22:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0009_auto_20180826_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiAppConfigModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('childApp', models.ForeignKey(help_text='Relevant apps', on_delete=django.db.models.deletion.CASCADE, to='home.ApplicationDefinitionModel', verbose_name='Child apps')),
            ],
        ),
        migrations.CreateModel(
            name='MultiAppModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueId', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Unique ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='multiappconfigmodel',
            name='pathInstance',
            field=models.ForeignKey(help_text='Relevant Model', on_delete=django.db.models.deletion.CASCADE, to='multiapp.MultiAppModel', verbose_name='MultiApp'),
        ),
    ]