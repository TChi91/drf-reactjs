<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-07-20 20:00
=======
# Generated by Django 3.0.8 on 2020-07-21 21:46
>>>>>>> eaf6b721a7d15e744899e59f9f558cdb1de72ff1

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
    ]
