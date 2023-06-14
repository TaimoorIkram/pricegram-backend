from rest_framework import serializers
from restbase.models import Product, ViewHistory, Favourite, SearchHistory, VisitHistory, Like
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

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
        model = Favourite
        fields = '__all__'
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email')
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
    )
    user.set_password(validated_data['password'])
    user.save()
    return user