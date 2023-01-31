# Generated by Django 3.1.12 on 2022-01-18 07:50

from django.db import migrations, models
import djongo.models.fields
import myapi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mypost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pusername', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=200)),
                ('like', djongo.models.fields.EmbeddedField(model_container=myapi.models.Like)),
                ('TotalLike', models.IntegerField(default=0)),
            ],
        ),
    ]
