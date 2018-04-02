# Generated by Django 2.0.2 on 2018-02-09 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180207_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_set', to='main.School'),
        ),
        migrations.AddField(
            model_name='player',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.PlayerRole'),
        ),
    ]