from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0007_drawingtemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawingtemplate',
            name='tool',
            field=models.CharField(default='LineTool', max_length=200),
            preserve_default=False,
        ),
    ]
