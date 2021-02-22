# Generated by Django 3.1 on 2020-08-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, verbose_name='title')),
                ('detail', models.TextField(verbose_name='detail')),
                ('published_on', models.DateField(auto_now_add=True)),
                ('fb_link', models.URLField(max_length=400)),
                ('attachment', models.URLField(max_length=400)),
                ('category', models.CharField(choices=[('Placements', 'Placements'), ('Achivements', 'Achivements'), ('Examinations', 'Examinations'), ('Scholarships', 'Scholarships'), ('Activities', 'Activities'), ('Other', 'Other')], default='Other', max_length=100)),
            ],
        ),
    ]
