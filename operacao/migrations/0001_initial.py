# Generated by Django 4.2.7 on 2023-11-10 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.CharField(max_length=200, verbose_name='Número 1')),
                ('num2', models.CharField(max_length=200, verbose_name='Número 2')),
                ('op', models.CharField(max_length=2, verbose_name='Operação')),
                ('result', models.CharField(max_length=200, verbose_name='Resultado')),
                ('data', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Submissão')),
            ],
            options={
                'ordering': ['data'],
            },
        ),
    ]
