# Generated by Django 4.0.3 on 2022-03-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0002_film_rok_alter_film_tytul'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='imdb_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='opis',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='film',
            name='plakat',
            field=models.ImageField(blank=True, null=True, upload_to='plakaty'),
        ),
        migrations.AddField(
            model_name='film',
            name='premiera',
            field=models.DateField(blank=True, null=True),
        ),
    ]
