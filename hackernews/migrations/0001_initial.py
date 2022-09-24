# Generated by Django 4.0.7 on 2022-09-24 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hacker_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('by', models.CharField(max_length=100, verbose_name='Author')),
                ('time', models.DateTimeField()),
                ('hacker_url', models.URLField(blank=True, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hackernews.postbase')),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('hackernews.postbase',),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hackernews.postbase')),
                ('score', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('hackernews.postbase',),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hackernews.postbase')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('score', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('hackernews.postbase',),
        ),
        migrations.CreateModel(
            name='PollOption',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hackernews.postbase')),
                ('score', models.IntegerField()),
                ('text', models.TextField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', related_query_name='option', to='hackernews.poll')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('hackernews.postbase',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hackernews.postbase')),
                ('text', models.TextField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kids', related_query_name='kid', to='hackernews.postbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('hackernews.postbase',),
        ),
    ]
