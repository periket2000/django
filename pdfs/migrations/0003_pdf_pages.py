# Generated by Django 3.2.9 on 2021-12-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfs', '0002_pdf_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='pages',
            field=models.IntegerField(default=0),
        ),
    ]
