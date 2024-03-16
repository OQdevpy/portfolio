# Generated by Django 4.2.4 on 2024-03-16 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_about_description_en_about_description_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.project'),
        ),
        migrations.AddField(
            model_name='project',
            name='techs',
            field=models.ManyToManyField(blank=True, null=True, related_name='techs', to='home.technology'),
        ),
    ]