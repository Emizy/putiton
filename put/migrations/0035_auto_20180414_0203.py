# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-14 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('put', '0034_auto_20180414_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Clothing', 'Clothing'), ('Hairstylist', 'Hairstylist'), ('Jewelry', 'Jewelry'), ('Beads', 'Beads'), ('Shoes', 'Shoes'), ('Watches', 'Watches'), ('WeddingWears', 'WeddingWears'), ('MakeupArtist', 'MakeupArtist'), ('Bags', 'Bags')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='post_view',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='supp_ads',
            name='category',
            field=models.CharField(blank=True, choices=[('men_acc', 'men_acc'), ('beads', 'beads'), ('makeup', 'makeup'), ('men', 'men'), ('women', 'women')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='confirm',
            field=models.CharField(blank=True, choices=[('UNAPPROVED', 'UNAPPROVED'), ('APPROVED', 'APPROVED'), ('Nil', 'Nil')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='status',
            field=models.CharField(blank=True, choices=[('Platinum', 'Platinum'), ('Free', 'Free'), ('Gold', 'Gold'), ('NoSub', 'NoSub'), ('Silver', 'Silver')], max_length=20, null=True),
        ),
    ]
