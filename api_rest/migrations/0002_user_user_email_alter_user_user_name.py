# Generated by Django 4.2.4 on 2023-09-02 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=150),
        ),
    ]