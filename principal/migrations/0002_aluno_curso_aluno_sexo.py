# Generated by Django 4.1.3 on 2022-11-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.CharField(choices=[('Curso Técnico', 'Curso Técnico')], default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='', max_length=150),
            preserve_default=False,
        ),
    ]
