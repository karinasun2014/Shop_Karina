from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Product', views.ProductViewSet)
router.register(r'Category', views.CategoryViewSet)
router.register(r'Img', views.ImgViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]