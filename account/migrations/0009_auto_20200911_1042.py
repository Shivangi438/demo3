# Generated by Django 3.1 on 2020-09-11 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0008_auto_20200910_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_timetable',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher_timetable',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]