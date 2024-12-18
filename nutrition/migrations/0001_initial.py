# Generated by Django 5.1.4 on 2024-12-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.PositiveIntegerField()),
                ('protein', models.PositiveIntegerField(default=0)),
                ('carbs', models.PositiveIntegerField(default=0)),
                ('fat', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgressLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.PositiveIntegerField(help_text="Track the user's progress (e.g., calorie intake)")),
                ('date', models.DateField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
