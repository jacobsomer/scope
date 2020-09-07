# Generated by Django 3.0.5 on 2020-09-07 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sourcing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCode',
            fields=[
                ('activity_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('activity_desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ActorCode',
            fields=[
                ('actor_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('actor_desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StatusCode',
            fields=[
                ('status_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('status_desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_date', models.DateField()),
                ('fuzzy_date', models.CharField(blank=True, max_length=30, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('activity_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activities', to='parsing.ActivityCode')),
                ('actor_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activities', to='parsing.ActorCode')),
                ('source_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sourcing.Source')),
                ('status_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='parsing.StatusCode')),
            ],
        ),
    ]
