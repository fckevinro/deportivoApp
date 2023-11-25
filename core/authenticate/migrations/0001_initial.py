# Generated by Django 4.2.5 on 2023-11-14 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plantel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/media/')),
            ],
            options={
                'verbose_name': 'Plantel',
                'verbose_name_plural': 'Planteles',
            },
        ),
        migrations.CreateModel(
            name='UserRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_medico', models.CharField(default='Disponible', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/media/')),
                ('plantel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authenticate.plantel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
