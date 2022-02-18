# ViewSet
- generics APIView를 통해서 코드를 많이 감소화 했지만, 그래도 재사용성이 부족한 느낌이였다.
- 그래서 ViewSet이라는 클래스를 만들어 generics APIView를 통합하였다.
- ViewSet은 CBV가 아닌 펠커플래스로 두가지 종류가 있다.
  + viewsets.ReadOnlyModelViewSet : 목록 조회, 특정 레코드 조회
  + viewsets.ModelViewSet : 목록 조회, 특정 레코드 생성/조회/수정/삭제

```python
# serializers.py
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

# views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny] # POST조회시는 AllowAny속성을 쓰면 안된다.

```
---
- generics와 차이점은 ModelViewSet이라는 것으로 하나로 통합 되었다는 것이다.
- ViewSet은 위와 같이 작성하고 path에 관한 내용을 추가적으로 기입해야하는데 
- /post/ <- 이렇게 하나만 넣어도 Restful API가 구동 되도록 하기 위함이다.

```python
#urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
- 위와 같이 작성하여야 ViewSet을 온전히 사용할 수 있다.
- /posts/ 로 들어 왔을 때는 GET(리스트 조회), POST(post 생성)
- /posts/<int:pk> 로 들어 왔을 때는 GET, PUT, DELETE 등을 처리해준다
- ViewSet은 posts 주소 하나로 모든 것을 처리해 주는 것이다.




- ViewSet 속성 처리한것 정리해야함
