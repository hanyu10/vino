# Generated by Django 3.2.6 on 2021-08-06 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0001_initial'),
        ('review', '0002_post_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='wine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wine.wine', verbose_name='OWNER'),
        ),
    ]