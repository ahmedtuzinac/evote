# Generated by Django 4.1.5 on 2023-01-18 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eVote_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='citizen',
            name='town',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='citizens', to='eVote_app.town'),
            preserve_default=False,
        ),
    ]
