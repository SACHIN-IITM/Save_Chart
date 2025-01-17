from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_study_templates_indexes'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrawingTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerSource', models.CharField(db_index=True, max_length=200)),
                ('ownerId', models.CharField(db_index=True, max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('content', jsonfield.fields.JSONField()),
            ],
        ),
    ]
