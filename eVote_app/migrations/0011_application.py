# Generated by Django 4.1.5 on 2023-01-19 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eVote_app', '0010_remove_politicalparty_politicanelection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('politicalelection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eVote_app.politicalelection')),
                ('politicalparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eVote_app.politicalparty')),
            ],
        ),
    ]
