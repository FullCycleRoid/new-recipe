# Generated by Django 2.1.15 on 2020-04-25 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='path/')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Recipe')),
            ],
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]
