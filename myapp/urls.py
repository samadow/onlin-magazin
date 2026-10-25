from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("category", CategoriApi, basename="category")
router.register("product", ProductApi, basename="product")


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("product/search/", poisk_product),
    path("product/filter/", filter_product),
    path("Cart_c",creat_cart.as_view()),
    path("cart_detail/<int:pk>/", deatil_cart.as_view()),
    path("cart-item-cr",creat_cartitem.as_view()),
    path("cart-item-detail/<int:pk>",deatil_cartitem.as_view()),
    path("cart-item-delete/<int:pk>/",DeleteCartItem.as_view(),name="cart-item-delete"),
    path("orders_creat/",OrderDetailView.as_view()),
    path("orders_detail/<int:pk>/",OrderDetailView.as_view()),
    path("orders_lisst/<int:pk>/",OrderlistView.as_view()),
    path("orders_delet/<int:pk>/",OrderdeletView.as_view()),
    path("admin/orders/<int:pk>/status/",OrderStatusUpdateView.as_view(),name="order-status-update"),
    path('', include(router.urls)),
    
]


