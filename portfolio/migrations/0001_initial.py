# Generated by Django 4.2.7 on 2023-11-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('tecno', models.CharField(default='Sin especificar', max_length=250)),
                ('url', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
            ],
        ),
    ]
