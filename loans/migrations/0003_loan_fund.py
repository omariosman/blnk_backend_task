# Generated by Django 3.2.7 on 2021-10-05 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loans', '0002_auto_20211005_0340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.loan_template')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]