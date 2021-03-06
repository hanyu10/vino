# Generated by Django 3.2.6 on 2021-08-09 11:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0004_auto_20210806_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='post',
            name='wine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wine.wine', verbose_name='와인'),
        ),
    ]
