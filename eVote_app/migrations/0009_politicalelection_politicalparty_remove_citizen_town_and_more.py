# Generated by Django 4.1.5 on 2023-01-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eVote_app', '0008_remove_choices_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalElection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PoliticalParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=200)),
                ('politicanelection', models.ManyToManyField(to='eVote_app.politicalelection')),
            ],
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='town',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
        migrations.DeleteModel(
            name='Citizen',
        ),
        migrations.DeleteModel(
            name='Town',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]