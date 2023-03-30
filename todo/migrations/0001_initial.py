# Generated by Django 3.2.8 on 2022-10-04 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Заголовок проекта', max_length=24)),
                ('linkGitHub', models.URLField(blank=True, help_text='Ссылка на репозиторий GitHub', null=True)),
                ('users', models.ManyToManyField(to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, help_text='поле для заметок', null=True)),
                ('create_publish', models.DateField(auto_now_add=True, help_text='поле даты создания заметки')),
                ('update_publish', models.DateField(auto_now=True, help_text='поле даты обновления заметки')),
                ('status', models.CharField(choices=[('a', 'active'), ('с', 'closed')], help_text='поле статуса,активная или закрыта', max_length=1)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todo.project')),
                ('users', models.ForeignKey(blank=True, help_text='поля авто заметки', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
