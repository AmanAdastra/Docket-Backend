from shortcut.views import ShortcutCreateApi,ShortcutListApi
from django.urls import path


urlpatterns=[
    path('create/', ShortcutCreateApi.as_view()),
    path('list/', ShortcutListApi.as_view()),
]