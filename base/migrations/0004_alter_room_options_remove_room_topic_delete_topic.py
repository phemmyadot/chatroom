# Generated by Django 4.2.1 on 2023-05-30 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updatedAt', '-createdAt']},
        ),
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]