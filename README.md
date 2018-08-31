# DJANGO UEditor Plugins
This project provide the ability for easy use UEditor in django admin and other pages in django.

Many code is from other project, such as: django-ckeditor and so on.

### Required
1. Install or add django-ueditor to your environment.
    ```
    pip install django-ueditor
    ```
2. add `ueditor` to your `INSTALLED_APPS` setting.
3. add UEditor URL include to your project's `urls.py` file:
    ```
    re_path(r'^ueditor/', include('ueditor.urls')),
    ```
### Usage

##### Field

The quickest way to add rich text editing capabilities to your models is to use the `UEditorField` model field type.
For example:
```
from django.db import models
from ueditor import UEditorField

class Post(models.Model):
    content = UEditorField('内容')
```

That's all you need to do, enjoy the plugins and feel free to contact me when you has any problem with it.
