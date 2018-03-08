# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-05 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('put', '0013_auto_20180221_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='username',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='supplier',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='packages',
            name='status',
            field=models.CharField(blank=True, choices=[('Silver', 'Silver'), ('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Free', 'Free')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('men_acc', 'men_acc'), ('makeupArtist', 'makeupArtist'), ('women', 'women'), ('men', 'men'), ('hairstyle', 'hairstyle'), ('makeup', 'makeup'), ('beads', 'beads')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('Silver', 'Silver'), ('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Free', 'Free')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supp_ads',
            name='category',
            field=models.CharField(blank=True, choices=[('men_acc', 'men_acc'), ('women', 'women'), ('men', 'men'), ('makeup', 'makeup'), ('beads', 'beads')], max_length=20, null=True),
        ),
    ]