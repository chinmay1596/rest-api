from django.urls import path, include
from . import views
from .views import ArticleAPIView, DetailAPIView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter ()
router.register('article', ArticleViewSet, basename='article')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),


    #path('article/', views.article_list, name='article'),
    path('article/', ArticleAPIView.as_view(), name='article'),
    #path('detail/<int:pk>/', views.article_detail, name='article-detail'),
    path('detail/<int:id>/', DetailAPIView.as_view(), name='detail'),
    path('generic/article/<int:id>/', GenericAPIView.as_view(), name='generic-article'),
]