from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)
# post_list, post_detail의 2개 url을 자동으로 만들어줌 router.urls에 있음

urlpatterns = [
    path('', include(router.urls)),
]