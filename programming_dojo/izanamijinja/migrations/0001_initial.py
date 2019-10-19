# Generated by Django 2.2 on 2019-10-19 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ryugi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('na', models.CharField(max_length=20)),
                ('kotodute', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Kata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kataki', models.TextField()),
                ('waza1', models.CharField(max_length=40)),
                ('waza2', models.CharField(blank=True, max_length=40)),
                ('waza3', models.CharField(blank=True, max_length=40)),
                ('rendo', models.CharField(choices=[('0', 'Mijuku'), ('1', 'Nami'), ('2', 'Jukuren')], default='0', max_length=1)),
                ('ryugi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='izanamijinja.Ryugi')),
            ],
        ),
    ]