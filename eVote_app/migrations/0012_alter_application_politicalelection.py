# Generated by Django 4.1.5 on 2023-01-19 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eVote_app', '0011_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='politicalelection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selectionlist', to='eVote_app.politicalelection'),
        ),
    ]