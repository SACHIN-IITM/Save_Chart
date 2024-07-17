from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_chart_indexes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studytemplate',
            name='ownerId',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='studytemplate',
            name='ownerSource',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
