from shortcut.models import Shortcut
from shortcut.serializers import ShortcutSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class ShortcutCreateApi(generics.CreateAPIView):
    serializer_class = ShortcutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        name = request.data.get('name')
        url = request.data.get('url')
        if not name:
            return Response({'error': 'name is required'})
        if not url:
            return Response({'error': 'url is required'})
        Shortcut.objects.create(user=user, name=name, url=url)
        return Response({'status': 'ok'})

class ShortcutListApi(generics.ListAPIView):
    serializer_class = ShortcutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Shortcut.objects.filter(user=user)