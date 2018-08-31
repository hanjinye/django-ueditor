# coding: utf-8
# License: MIT, see LICENSE.txt

from __future__ import absolute_import
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

DEFAULT = {}
CONFIG = getattr(settings, 'UEDITOR_DEFAULT_CONFIG', DEFAULT)
CONFIG_URL = staticfiles_storage.url('/ueditor/ueditor.config.js')
JS_URL = getattr(settings, 'UEDITOR_JS_URL', None)
if JS_URL is None:
    JS_URL = staticfiles_storage.url('ueditor/ueditor.all.min.js')

