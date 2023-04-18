# Generated by Django 4.2 on 2023-04-17 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=64)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ProxyEmployee1',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('AdvancedModeConcepts.employee',),
        ),
        migrations.CreateModel(
            name='ProxyEmployee2',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('AdvancedModeConcepts.employee',),
        ),
    ]
