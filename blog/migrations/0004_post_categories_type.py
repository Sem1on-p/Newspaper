# Generated by Django 3.2 on 2021-06-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories_type',
            field=models.CharField(blank=True, choices=[('R', 'Важно'), ('O', 'Срочно')], max_length=1, verbose_name='Метки'),
        ),
    ]
