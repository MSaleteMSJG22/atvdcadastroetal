# Generated by Django 4.1.3 on 2022-11-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_aluno_curso_aluno_sexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='minicursos',
            field=models.ManyToManyField(to='principal.minicurso'),
        ),
    ]
