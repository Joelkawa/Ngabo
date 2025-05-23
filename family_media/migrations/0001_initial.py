# Generated by Django 5.1.5 on 2025-02-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField(max_length=250)),
                ('images', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('date_added', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
