# Generated by Django 4.2.5 on 2023-11-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0006_alter_lead_priority_alter_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('contacted', 'Contacted'), ('won', 'Won'), ('new', 'New'), ('lost', 'Lost')], default='new', max_length=10),
        ),
    ]
