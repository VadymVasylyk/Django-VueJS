from rest_framework.serializers import ModelSerializer
from .models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemEditSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'