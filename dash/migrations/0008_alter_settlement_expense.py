# Generated by Django 4.1.3 on 2023-06-08 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_alter_settlement_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settlement',
            name='expense',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dash.expense'),
        ),
    ]
