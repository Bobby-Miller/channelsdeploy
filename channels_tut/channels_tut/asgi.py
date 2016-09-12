"""
WSGI config for channels_tut project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channels_tut.settings")
channel_layer = channels.asgi.get_channel_layer()