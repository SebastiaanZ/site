# Generated by Django 2.1.2 on 2018-12-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField()),
                ('summary', models.CharField(max_length=280)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
