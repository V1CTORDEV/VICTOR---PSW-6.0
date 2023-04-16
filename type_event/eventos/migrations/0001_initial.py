# Generated by Django 4.2 on 2023-04-15 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('carga_horario', models.IntegerField()),
                ('logo', models.ImageField(upload_to='logos')),
                ('cor_principal', models.CharField(max_length=7)),
                ('cor_secundaria', models.CharField(max_length=7)),
                ('cor_fundo', models.CharField(max_length=7)),
            ],
        ),
    ]
