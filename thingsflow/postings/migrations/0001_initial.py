# Generated by Django 3.1.3 on 2022-09-06 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=20)),
                ('context', models.CharField(max_length=200)),
                ('psword', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'postings',
            },
        ),
    ]