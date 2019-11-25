# Generated by Django 2.1 on 2019-04-14 19:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):


    dependencies = [
        ('home', '0007_auto_20190414_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicemodel',
            name='id',
            field=models.AutoField(auto_created=True, default=202904467276636910751124456160804894152, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='devicemodel',
            name='deviceId',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]