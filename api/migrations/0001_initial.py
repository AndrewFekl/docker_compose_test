# Generated by Django 3.1 on 2022-01-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCorrelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.JSONField()),
                ('x_data_type', models.CharField(max_length=100)),
                ('y_data_type', models.CharField(max_length=100)),
                ('correlation', models.JSONField()),
            ],
        ),
    ]
