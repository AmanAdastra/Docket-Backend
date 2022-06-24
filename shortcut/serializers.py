from shortcut.models import Shortcut
from rest_framework import serializers

class ShortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortcut
        fields = ('id','name','url','created_at','updated_at')
