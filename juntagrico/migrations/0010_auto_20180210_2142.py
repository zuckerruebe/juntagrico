# Generated by Django 2.0.2 on 2018-02-10 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juntagrico', '0009_auto_20180206_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depot',
            name='addr_location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ort'),
        ),
        migrations.AlterField(
            model_name='depot',
            name='addr_street',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Strasse'),
        ),
        migrations.AlterField(
            model_name='depot',
            name='addr_zipcode',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='PLZ'),
        ),
        migrations.AlterField(
            model_name='depot',
            name='latitude',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='depot',
            name='longitude',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='tfsst',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='TTFSST', to='juntagrico.SubscriptionType'),
        ),
        migrations.AlterField(
            model_name='tsst',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='TTSST', to='juntagrico.SubscriptionType'),
        ),
    ]