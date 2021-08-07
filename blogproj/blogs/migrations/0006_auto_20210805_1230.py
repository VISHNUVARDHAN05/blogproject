# Generated by Django 3.2.6 on 2021-08-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('uncategorised', 'uncategorised'), ('mobiles', 'mobiles'), ('cars', 'cars'), ('uncategorised', 'uncategorised'), ('education', 'education')], default='uncategorised', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(),
        ),
    ]