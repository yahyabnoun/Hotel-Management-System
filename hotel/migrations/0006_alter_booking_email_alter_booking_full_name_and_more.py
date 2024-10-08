# Generated by Django 5.0.6 on 2024-09-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_alter_roomtype_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='num_adults',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending'), ('Processing', 'Processing'), ('cancelled', 'cancelled'), ('initiated', 'initiated'), ('failed', 'failed'), ('refunding', 'refunding'), ('refunded', 'refunded'), ('unpaid', 'unpaid'), ('expired', 'expired')], default='pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
