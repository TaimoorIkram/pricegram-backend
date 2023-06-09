from rest_framework import serializers
from restbase.models import Product, ViewHistory, Favourite, SearchHistory, VisitHistory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewHistory
        fields = '__all__'

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = '__all__'

class VisitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitHistory
        fields = '__all__'


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model =Favourite
        fields = '__all__'