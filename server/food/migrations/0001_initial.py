# Generated by Django 4.2.8 on 2023-12-29 22:42

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=False)),
                ('food_group_id', models.ForeignKey('FoodGroup', null=False, serialize=False, on_delete = models.CASCADE))
            ],
            options={
                'db_table': 'Food',
                'managed': True
            },
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=False)),
            ],
            options={
                'db_table': 'Food_Group',
                'managed': True
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=False)),
            ],
            options={
                'db_table': 'Recipe',
                'managed': True
            },
        ),
        migrations.CreateModel(
            name='RecipeFood',
            fields=[
                ('recipe_id', models.ForeignKey('Recipe', null=False, serialize=False, on_delete = models.CASCADE)),
                ('food_id', models.ForeignKey('Food', null=False, serialize=False, on_delete = models.CASCADE))
            ],
            options={
                'db_table': 'Recipe_Food',
                'managed': True
            },
        ),
    ]
