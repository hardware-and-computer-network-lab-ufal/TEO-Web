# Generated by Django 2.2.2 on 2019-06-18 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('cnpj', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('endereco', models.CharField(max_length=45)),
                ('contato', models.CharField(max_length=45)),
            ],
        ),
    ]
