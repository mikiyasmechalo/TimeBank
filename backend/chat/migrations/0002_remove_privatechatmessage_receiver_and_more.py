# Generated by Django 5.2 on 2025-05-08 07:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="privatechatmessage",
            name="receiver",
        ),
        migrations.RemoveField(
            model_name="privatechatmessage",
            name="sender",
        ),
        migrations.DeleteModel(
            name="ChatMessage",
        ),
        migrations.DeleteModel(
            name="PrivateChatMessage",
        ),
    ]
