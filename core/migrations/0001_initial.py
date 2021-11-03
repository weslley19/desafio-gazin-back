# Generated by Django 3.2.4 on 2021-11-03 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('age', models.IntegerField(verbose_name='Idade')),
                ('hobby', models.TextField(max_length=255, verbose_name='Hobby')),
                ('birthdate', models.DateField(verbose_name='Data de nascimento')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            bases=('core.base',),
        ),
    ]
