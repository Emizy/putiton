# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-09 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('put', '0023_auto_20180309_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='sub_date',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Beads', 'Beads'), ('Hairstylist', 'Hairstylist'), ('Shoes', 'Shoes'), ('WeddingWears', 'WeddingWears'), ('Clothing', 'Clothing'), ('Jewelry', 'Jewelry'), ('Watches', 'Watches'), ('Bags', 'Bags'), ('MakeupArtist', 'MakeupArtist')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supp_ads',
            name='category',
            field=models.CharField(blank=True, choices=[('men', 'men'), ('women', 'women'), ('beads', 'beads'), ('men_acc', 'men_acc'), ('makeup', 'makeup')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='confirm',
            field=models.CharField(blank=True, choices=[('Nil', 'Nil'), ('UNAPPROVED', 'UNAPPROVED'), ('APPROVED', 'APPROVED')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='status',
            field=models.CharField(blank=True, choices=[('Free', 'Free'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('NoSub', 'NoSub'), ('Platinum', 'Platinum')], max_length=20, null=True),
        ),
    ]
