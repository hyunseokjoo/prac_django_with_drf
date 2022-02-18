# ModelSerializer란?
- DRF에서는 Restful API를 지원하기 위해 Serializer객체를 이용한 직렬화, ModelSerializer를 이용한 직렬화를 지원합니다.
- Django에서 사용하는 ModelForm과 유사하며, ModelSerializer를 이용하여 데이터를 손쉽게 직렬화 할 수 있습니다.

```python
# models.py
from django.db import models

# person 이라는 모델 생성
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# serializers.py 
from rest_framework.serializers import ModelSerializer
from .models from Person

# model을 이용한 modelserializer생성
class PersonSerializer(ModelSerializer):
    class Meta:
        models = Person
        fields = ['id', 'name', 'age']

qs = Person.Objects.all()
serializer = PersonSerializer(qs, many=True)
response = Response(serializer.date)

```