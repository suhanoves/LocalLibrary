# Generated by Django 3.2.5 on 2021-08-11 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'permissions': (('can_author_edit', 'Create, update and delete Author'),), 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
    ]