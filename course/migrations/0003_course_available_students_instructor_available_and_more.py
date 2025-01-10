# Generated by Django 5.1.4 on 2025-01-09 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_courses_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Available',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('joined_in', models.DateTimeField(auto_now_add=True)),
                ('course_period', models.IntegerField()),
                ('student_number', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor_Available',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('joined_in', models.DateTimeField(auto_now_add=True)),
                ('student_number', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=50)),
                ('course_assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course_available')),
            ],
        ),
        migrations.AddField(
            model_name='course_available',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.instructor_available'),
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
    ]
