# Generated by Django 4.1.4 on 2022-12-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main2', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sound', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='Main2/static'),
        ),
    ]
