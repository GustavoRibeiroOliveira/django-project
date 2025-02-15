# Generated by Django 5.0.6 on 2024-06-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_estado_pais_cidade_estado_estado_pais'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estado',
            options={'ordering': ('nome',)},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'País', 'verbose_name_plural': 'Países'},
        ),
        migrations.AddField(
            model_name='cidade',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
    ]
