# Generated by Django 5.1.3 on 2024-12-03 15:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('NomChauffeur', models.CharField(max_length=100)),
                ('plaque', models.CharField(max_length=100)),
                ('NbrPlaceVide', models.IntegerField()),
                ('VilleDepart', models.CharField(max_length=100)),
                ('VilleArrivee', models.CharField(max_length=100)),
                ('heureDepart', models.TimeField()),
                ('Prix', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='voyages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Escale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VilleEscale', models.CharField(max_length=100)),
                ('NbrPlaceAjouter', models.IntegerField(null=True)),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escales', to='voyage.voyage')),
            ],
        ),
    ]
