# generics APIView
- APIView는 request.method별로 다 정의 해야 하기 때문에 재사용성이 조금 떨어집니다.
- Mixin란 create, retrieve, update등을 처리해주는 DRF클래스들인데 이 mixin을 상속받아 처리하면 APIView재상용성을 높일 수 있다. 
- generics APIView는 Mixin을 상속받아 메소드별로 처리 되는 로직을 새로운 클래스로 정의해 놓은 클래스이다.
- generics APIView 종류
  + generics.CreateAPIView : 생성
  + generics.ListAPIView : 목록
  + generics.RetrieveAPIView : 조회
  + generics.DestroyAPIView : 삭제
  + generics.UpdateAPIView : 수정
  + generics.RetrieveUpdateAPIView : 조회/수정
  + generics.RetrieveDestroyAPIView : 조회/삭제
  + generics.ListCreateAPIView : 목록/생성
  + generics.RetrieveUpdateDestroyAPIView : 조회/수정/삭제

# 예시1
```python
# views.py

from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

# APIView에서 
# /person/  List = GET , Create = POST
class PersonListGenericAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
# /person/<int:pk> Retrieve = GET, Update = PUT, Destroyl = DELETE
class PersonDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
```
---
# 예시2
- Create와 Update등을 serializers에서 재정의해서 사용가능하다.
```python
# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_date):
        user = User.objects.create(validated_date['username'])
        user.set_password(validated_date['password'])
        user.save()
        return user# 암호화하는 로직

    class Meta:
        model = User
        fields = ['pk', 'username', 'password']

# views.py
class SignupView(CreateAPIView):
     model = get_user_model() # settings.AUTH_USER_MODEL를 가져옴 //accounts/user
     serializer_class = SignupSerializer
     permission_classes = [
         AllowAny,
     ]

# urls.py
from django.urls import path
from . import views

urlpatterns =[
    path('signup/', views.SignupView.as_view(), name='login')
]
```

