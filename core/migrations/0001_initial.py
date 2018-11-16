# Generated by Django 2.1.3 on 2018-11-15 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=100, null=True)),
                ('body', models.TextField()),
                ('images_srcs', models.TextField()),
                ('anchor_links', models.TextField()),
                ('anchor_texts', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='website',
            unique_together={('website_name', 'title')},
        ),
        migrations.AddField(
            model_name='blogdata',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Website'),
        ),
    ]
