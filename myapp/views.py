from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .models import *
from rest_framework.decorators import api_view


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]



class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

class ProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class CategoriApi(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
class ProductApi(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    


@api_view(["GET"])
def poisk_product(request):
    name = request.query_params.get("name", "")
    products = Product.objects.filter(name__icontains=name)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def filter_product(request):
    category = request.query_params.get("category")
    max_price = request.query_params.get("max_price")
    products = Product.objects.all()
    
    if category:
        products = products.filter(categori_id=category)
    if max_price:
        products = products.filter(price__lte=max_price)
        
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# 
class creat_cart(generics.CreateAPIView):
    serializer_class = CartSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)

        serializer = self.get_serializer(cart)

        if not created:
            return Response({"message": "Шумо аллакай корзина доред."},status=status.HTTP_200_OK)

        return Response( serializer.data, status=status.HTTP_201_CREATED)

class deatil_cart(generics.ListAPIView):
    serializer_class = CartSerializers
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    
    
    

class creat_cartitem(generics.CreateAPIView):
    queryset = Cart_item.objects.all()
    serializer_class = Cart_itemSerialiser
    permission_classes = [permissions.IsAuthenticated]

    

class deatil_cartitem(generics.ListAPIView):
    serializer_class = Cart_itemSerialiser
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Cart_item.objects.filter(cart__user=self.request.user)
    

    
    
class DeleteCartItem(generics.DestroyAPIView):
    serializer_class = Cart_itemSerialiser
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart_item.objects.filter(cart__user=self.request.user)

    


class Ordercreat(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    
    
class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    
    
class OrderlistView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)



class OrderdeletView(generics.DestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)



class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]