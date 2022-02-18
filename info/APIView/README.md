# APIView 사용하기
- 순서
  + APIView와 api_view란?
  + APIView를 이용한 메소드별 처리법 실습(get,post), (get, delete, put)
  + Mixins
  + genericsView란?
  + ViewSet이란?
### APIView와 api_view란?
--- 
- DRF에서 Restful API를 지원하기 위해 사용하는 로직이 있는 클래스 라고 보면된다.
- APIView와 @api_view는 CBV와 FBV에 대응한다.
---
### APIView를 사용하여 지원하는 기본 설정
  + 직렬화 클래스 
    + renderer_classes
    + default 
      + JSON 직렬화 : rest_framework.renderers.JSONRenderer
      + HTML 페이지 직렬화 : rest_framework.renderers.TemplateHTMLRenderer
  + 비직렬화 클래스 
    + parser_classes
    + default
      + JSON 포맷 처리 : rest_framework.parsers.JSONParser
      + FormParser : rest_framework.parsers.FormParser
      + MultiPartParser : rest_framework.parsers.MultiPartParser
  + 인증 클래스 
    + authentication_classes
    + default 
      + 세션기반인증 : rest_framework.authentication.SessionAuthentication
      + HTTP basic 인증 : rest_framework.authentication.BasicAuthentication
  + 사용량 제한 클래스
    + throttle_classes
    + default
      + 빈 튜플
  + 권한 클래스 
    + permission_classes
    + default
      + 누구라도 접근 허용 : rest_framework.permissions.AllowAny
  + 요청에 따른 적절한 직렬화/비직렬화 선택
    + content_negotiation_class
    + default
      + rest_framework.negotiation.DefaultContentNegotiation
  + 요청내역세어 API 버전 정보를 탐지할 클래스
    + versioning_class
    + 요청 URL의 HEADER에서 버전 정보를 탐지하여 맞는 버전을 호출
    + default
      + 버전 정보를 탐지하지 않습니다. : None
  
---
### APIView
- /person/ 에 대한 CBV
  - get: 포스팅 목록
  - post: 새 포스팅 생성
- /person/<int:pk>/에 대한 CBV
  - get: pk에 해당하는 포스팅 내용
  - put: pk에 해당하는 포스팅 수정
  - delete: pk에 해당하는 포스팅 삭제

- 처리 순서 
  - 직렬화/비직렬화
  - 인증 체크
  - 사용량 제한 체크
  - 권한 체크
  - 요청한 버전 체크

- API처리를 위한 모델 생성
```python
#models.py 
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# serializers.py
from rest_framework.serializers import ModelSerializer
from .models import Person

class PersonSerializer(ModelSerializer):
    class Meta:
        models = Person
        fields = '__all__'
```

- APIView(CBV)를 이용한 request API 처리

```python
#Views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer

# /person/ 주소로 들어 왔을 때 API
class PersonListAPIView(APIView):
    def get(self, request):
        serializer = PersonSerializer(Person.objects.all(), many=True)
        return Response(serializer.data)
    
    def Post(self, request):
        serializer = PersonSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

from django.shortcuts import get_object_or_404
# /person/<int:pk> 주소로 들어 왔을 때 
class PesonDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Person, pk=pk)
    
    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk):
        person = self.get_object(pk)
        serializer = PersonSerializer(person)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAC_REQUEST)
    
    def delete(self,request, pk):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```




- APIView(FBV)를 이용한 request API 처리
```python
#urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    # FBV
    path('person/', views.PostListAPIView.as_view()),
    path('person/<int:pk>/',views.PostDetailAPIView.as_view()),
]
```


```python
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':
        qs = Person.objects.all()
        serializer = PersonSerializer(qs, many=True)
        return Response(serializer.data)
    else:
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE'])
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        serializer = PersonSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PersonSerializer(post, data=reqeust.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
```python 
# urls.py 
from django.urls import path, include 
from . import views 

urlpatterns = [ 
  # FBV 
  path('cbv/post/', views.post_list), 
  path('cbv/post/<int:pk>/',views.post_detail), 
]
```

---
-참조
[APIView 기본 클래스](https://ssungkang.tistory.com/entry/Django-APIView-Mixins-generics-APIView-ViewSet%EC%9D%84-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90)
[mixins](https://www.django-rest-framework.org/api-guide/generic-views/#mixins)
