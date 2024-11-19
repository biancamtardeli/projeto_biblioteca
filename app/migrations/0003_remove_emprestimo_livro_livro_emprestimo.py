# Generated by Django 5.1.3 on 2024-11-19 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_editora_cnpj_alter_editora_telefone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='livro',
        ),
        migrations.AddField(
            model_name='livro',
            name='emprestimo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.emprestimo'),
            preserve_default=False,
        ),
    ]