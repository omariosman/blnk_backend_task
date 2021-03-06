# Generated by Django 3.2.7 on 2021-10-07 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=1)),
                ('interest_rate', models.FloatField()),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('payments_number', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan_Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('taken', models.BooleanField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.loan_template')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('taken', models.BooleanField(blank=True, default=None, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.loan_template')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan_to_Loan_Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmt_out', models.FloatField(blank=True, null=True)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.loan1')),
                ('loan_fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.loan_fund')),
            ],
            options={
                'unique_together': {('loan', 'loan_fund')},
            },
        ),
    ]
