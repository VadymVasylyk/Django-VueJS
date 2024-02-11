from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .serializers import ItemSerializer, ItemEditSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Item


class ItemsPage(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemEdit(APIView):
    def put(self, req):
        item = get_object_or_404(Item, slug=req.data.get('slug'))
        serializer = ItemEditSerializer(item, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mess': 'Success'})
        return Response({'mess': 'Fail'})