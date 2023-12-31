# Generated by Django 4.2.5 on 2023-11-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0005_alter_lead_options_alter_lead_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('medium', 'Medium'), ('high', 'High'), ('low', 'Low')], default='medium', max_length=10),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('contacted', 'Contacted'), ('new', 'New'), ('lost', 'Lost'), ('won', 'Won')], default='new', max_length=10),
        ),
    ]
