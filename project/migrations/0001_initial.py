# Generated by Django 4.1.7 on 2023-05-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('marks', models.IntegerField()),
                ('email', models.EmailField(max_length=50, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('message', models.TextField(max_length=10000, null=True)),
            ],
        ),
    ]