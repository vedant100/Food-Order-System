# Generated by Django 3.1.1 on 2020-10-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.co.in/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Ffast-food-placeholder_34754&psig=AOvVaw2TqTHVt47YCefeNoJyOwhn&ust=1602259729195000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMCIqeiwpewCFQAAAAAdAAAAABAD', max_length=500),
        ),
    ]
