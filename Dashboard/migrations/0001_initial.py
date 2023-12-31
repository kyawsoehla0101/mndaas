# Generated by Django 4.2.2 on 2023-06-29 11:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('subcategory', models.CharField(choices=[('ST', 'Statment'), ('SP', 'Speech'), ('IN', 'Interview')], default='Statement', max_length=20)),
                ('category', models.CharField(choices=[('NA', 'NorthernAlliance'), ('FPNCC', 'FPNCC')], default='Northern Alliances', max_length=20)),
                ('image', models.ImageField(null=True, upload_to='alliance-images')),
                ('created', models.DateTimeField(auto_now=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('slug', models.SlugField(blank=True, default='', null=True, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('P', 'Party'), ('M', 'Military')], default='Party', max_length=20)),
                ('image', models.ImageField(null=True, upload_to='nation-images/')),
                ('created', models.DateTimeField(auto_now=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('ST', 'Statment'), ('SP', 'Speech'), ('IN', 'Interview')], default='Statement', max_length=20)),
                ('image', models.ImageField(null=True, upload_to='project-images')),
                ('created', models.DateTimeField(auto_now=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
