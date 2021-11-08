# Generated by Django 3.2.9 on 2021-11-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('viewer_hour', models.PositiveIntegerField()),
                ('hours_streamed', models.PositiveIntegerField()),
                ('acv_num', models.PositiveIntegerField()),
                ('creators', models.PositiveIntegerField()),
                ('streams_num', models.PositiveIntegerField()),
            ],
        ),
    ]
