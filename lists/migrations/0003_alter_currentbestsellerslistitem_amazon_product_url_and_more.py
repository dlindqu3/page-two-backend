# Generated by Django 4.0.5 on 2022-07-08 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_alter_currentbestsellerslistitem_amazon_product_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentbestsellerslistitem',
            name='amazon_product_url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='currentbestsellerslistitem',
            name='author',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='currentbestsellerslistitem',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='currentbestsellerslistitem',
            name='publisher',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='currentbestsellerslistitem',
            name='rank',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='currentbestsellerslistitem',
            name='title',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='currentbestsellerslistitem',
            name='weeks_on_list',
            field=models.IntegerField(),
        ),
    ]
