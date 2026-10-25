from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password','phon_number')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            phon_number = validated_data["phon_number"]
        )
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'fullname', 'phon_number')
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["name", "description", "guantiti", "price", "categori_id"]
        
        
class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["user"]


class Cart_itemSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Cart_item
        fields = ["cart","product", "quantity"]
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price"]
        
        
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "items"]
        