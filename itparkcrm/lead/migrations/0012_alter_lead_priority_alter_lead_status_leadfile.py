# Generated by Django 4.2.8 on 2023-12-21 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_plan_team_plan'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lead', '0011_alter_lead_priority_alter_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')], default='medium', max_length=10),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('lost', 'Lost'), ('contacted', 'Contacted'), ('won', 'Won')], default='new', max_length=10),
        ),
        migrations.CreateModel(
            name='LeadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='leadfiles')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_files', to=settings.AUTH_USER_MODEL)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='lead.lead')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_files', to='team.team')),
            ],
        ),
    ]
