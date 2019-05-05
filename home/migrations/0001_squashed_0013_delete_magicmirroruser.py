# Generated by Django 2.1 on 2019-04-14 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('home', '0001_initial'), ('home', '0002_auto_20180822_2115'), ('home', '0003_auto_20180822_2119'), ('home', '0004_auto_20180822_2125'), ('home', '0005_auto_20180822_2129'), ('home', '0006_auto_20180825_1848'), ('home', '0007_auto_20180826_1152'), ('home', '0008_auto_20180826_1154'), ('home', '0009_auto_20180826_1603'), ('home', '0010_phonenumbermodel'), ('home', '0011_auto_20181213_2155'), ('home', '0012_magicmirroruser'), ('home', '0013_delete_magicmirroruser')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationCSSFileBridgeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'App / CSS Bridge',
                'verbose_name_plural': 'App / CSS Bridges',
            },
        ),
        migrations.CreateModel(
            name='ApplicationDefinitionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Application Name')),
                ('bundlePath', models.CharField(max_length=100, verbose_name='Javascript Bundle Name')),
                ('hasCSS', models.BooleanField()),
                ('width_value', models.IntegerField(verbose_name='Width')),
                ('width_unit', models.CharField(max_length=10, verbose_name='Width Units')),
                ('height_value', models.IntegerField(verbose_name='Height')),
                ('height_unit', models.CharField(max_length=10, verbose_name='Height Units')),
            ],
            options={
                'verbose_name': 'Application Definition',
                'verbose_name_plural': 'Application Definitions',
            },
        ),
        migrations.CreateModel(
            name='ApplicationUIBridgeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'App UI Bridge',
                'verbose_name_plural': 'App UI Bridges',
            },
        ),
        migrations.CreateModel(
            name='ApplicationUIConfigModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startRow', models.IntegerField(help_text='The first row that this app should take up in the CSS Grid. Starts at 1', verbose_name='Start Row')),
                ('endRow', models.IntegerField(help_text='The last row that this app should take up in the CSS Grid. Exclusive', verbose_name='End Row')),
                ('startColumn', models.IntegerField(help_text='The first column that this app should take up in the CSS Grid. Starts at 1', verbose_name='Start Column')),
                ('endColumn', models.IntegerField(help_text='The last column that this app should take up in the CSS Grid. Exclusive', verbose_name='End Column')),
                ('name', models.CharField(help_text='Friendly name to refer to this UI configuration.', max_length=200, verbose_name='Name')),
                ('startOnStartup', models.BooleanField(verbose_name='Should Load On Start')),
            ],
            options={
                'verbose_name': 'App UI Configuration',
                'verbose_name_plural': 'App UI Configurations',
            },
        ),
        migrations.CreateModel(
            name='CSSResourceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourcePath', models.CharField(help_text='Location of the CSS file relative to the /static/ endpoint', max_length=100)),
            ],
            options={
                'verbose_name': 'CSS File',
                'verbose_name_plural': 'CSS Files',
            },
        ),
        migrations.CreateModel(
            name='FontModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Friendly name to use to refer to this font', max_length=200, verbose_name='Font Name')),
                ('url', models.CharField(help_text='URL to use to load the font', max_length=1000, verbose_name='Font URL')),
            ],
            options={
                'verbose_name': 'Font',
                'verbose_name_plural': 'Fonts',
            },
        ),
        migrations.CreateModel(
            name='MagicMirrorConfigModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField(help_text='Number of rows to use in the main MagicMirror grid', verbose_name='Rows')),
                ('columns', models.IntegerField(help_text='Number of columns to use in the main MagicMirror grid', verbose_name='Columns')),
                ('width_value', models.IntegerField(help_text='Number of whatever width unit desired', verbose_name='Width')),
                ('width_unit', models.CharField(choices=[('cm', 'Centimeters'), ('mm', 'Millimeters'), ('in', 'Inches'), ('px', 'Pixels'), ('pt', 'Points'), ('pc', 'Picas'), ('em', 'Relative to font-size'), ('ex', 'Relative to x-height'), ('ch', 'Relative to the "0" character'), ('rem', 'Relative to font size of root element'), ('vm', 'Relative to width of viewport'), ('vh', 'Relative to height of viewport'), ('vmin', 'Min of vm and vh'), ('vmax', 'Max of vm and vh'), ('%', 'Percent')], max_length=20)),
                ('height_value', models.IntegerField(help_text='Number of whatever column unit desired', verbose_name='Height')),
                ('height_unit', models.CharField(choices=[('cm', 'Centimeters'), ('mm', 'Millimeters'), ('in', 'Inches'), ('px', 'Pixels'), ('pt', 'Points'), ('pc', 'Picas'), ('em', 'Relative to font-size'), ('ex', 'Relative to x-height'), ('ch', 'Relative to the "0" character'), ('rem', 'Relative to font size of root element'), ('vm', 'Relative to width of viewport'), ('vh', 'Relative to height of viewport'), ('vmin', 'Min of vm and vh'), ('vmax', 'Max of vm and vh'), ('%', 'Percent')], max_length=20)),
                ('startUpApp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicationDefinitionModel')),
                ('configurationName', models.CharField(help_text='Friendly name to use to refer to this configuration', max_length=200)),
            ],
            options={
                'verbose_name': 'Magic Mirror Configuration',
                'verbose_name_plural': 'Magic Mirror Configurations',
            },
        ),
        migrations.CreateModel(
            name='UserAppListBridgeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicationDefinitionModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User App List',
                'verbose_name_plural': 'User App Lists',
            },
        ),
        migrations.AddField(
            model_name='applicationuibridgemodel',
            name='UI_Config',
            field=models.ForeignKey(help_text='UI configuration that defines how the app should appear', on_delete=django.db.models.deletion.CASCADE, to='home.ApplicationUIConfigModel', verbose_name='Configuration'),
        ),
        migrations.AddField(
            model_name='applicationuibridgemodel',
            name='app',
            field=models.ForeignKey(help_text='Application to use with a particular UI configuration', on_delete=django.db.models.deletion.CASCADE, to='home.ApplicationDefinitionModel', verbose_name='Application'),
        ),
        migrations.AddField(
            model_name='applicationcssfilebridgemodel',
            name='actualApp',
            field=models.ForeignKey(help_text='Application you want to associate a CSS File with', on_delete=django.db.models.deletion.CASCADE, to='home.ApplicationDefinitionModel', verbose_name='Application'),
        ),
        migrations.AddField(
            model_name='applicationcssfilebridgemodel',
            name='css_resource',
            field=models.ForeignKey(help_text='CSS file to be loaded when the application is loaded', on_delete=django.db.models.deletion.CASCADE, to='home.CSSResourceModel', verbose_name='CSS File'),
        ),
        migrations.AlterField(
            model_name='applicationdefinitionmodel',
            name='bundlePath',
            field=models.CharField(help_text='Location of the Javascript bundle that defines the app. Relative to the the /static/ endpoint', max_length=100, verbose_name='Javascript Bundle Name'),
        ),
        migrations.AlterField(
            model_name='applicationdefinitionmodel',
            name='name',
            field=models.CharField(help_text='Friendly name to use to refer to this application.', max_length=50, verbose_name='Application Name'),
        ),
        migrations.AlterField(
            model_name='applicationdefinitionmodel',
            name='height_unit',
            field=models.CharField(choices=[('cm', 'Centimeters'), ('mm', 'Millimeters'), ('in', 'Inches'), ('px', 'Pixels'), ('pt', 'Points'), ('pc', 'Picas'), ('em', 'Relative to font-size'), ('ex', 'Relative to x-height'), ('ch', 'Relative to the "0" character'), ('rem', 'Relative to font size of root element'), ('vm', 'Relative to width of viewport'), ('vh', 'Relative to height of viewport'), ('vmin', 'Min of vm and vh'), ('vmax', 'Max of vm and vh'), ('%', 'Percent')], max_length=20, verbose_name='Height Units'),
        ),
        migrations.AlterField(
            model_name='applicationdefinitionmodel',
            name='name',
            field=models.CharField(help_text='Friendly name to use to refer to this application.', max_length=200, verbose_name='Application Name'),
        ),
        migrations.AlterField(
            model_name='applicationdefinitionmodel',
            name='width_unit',
            field=models.CharField(choices=[('cm', 'Centimeters'), ('mm', 'Millimeters'), ('in', 'Inches'), ('px', 'Pixels'), ('pt', 'Points'), ('pc', 'Picas'), ('em', 'Relative to font-size'), ('ex', 'Relative to x-height'), ('ch', 'Relative to the "0" character'), ('rem', 'Relative to font size of root element'), ('vm', 'Relative to width of viewport'), ('vh', 'Relative to height of viewport'), ('vmin', 'Min of vm and vh'), ('vmax', 'Max of vm and vh'), ('%', 'Percent')], max_length=20, verbose_name='Width Units'),
        ),
    ]
