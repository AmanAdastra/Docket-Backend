# Generated by Django 4.0.5 on 2022-06-15 11:52

from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields
import questions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('level', django_enumfield.db.fields.EnumField(default=10, enum=questions.models.QuestionLevelType)),
                ('description', models.TextField()),
                ('code', models.TextField()),
                ('answer', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
