# Generated by Django 3.1.7 on 2021-04-03 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=200)),
                ('exchange', models.CharField(max_length=200)),
                ('signal', models.CharField(max_length=200)),
                ('volume', models.FloatField()),
                ('volumeindikator', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
                ('timenow', models.TimeField()),
                ('duration', models.DurationField()),
                ('orgm', models.CharField(max_length=200)),
                ('status', models.CharField(default='open', max_length=200)),
                ('previoustrade', models.IntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='polls.restaurant')),
            ],
        ),
    ]
