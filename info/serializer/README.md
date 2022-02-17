# Serializer

### Serializer(직렬화)란? 
---
- 통신을 진행할 때 데이터를 주고 받는 형식은 주로 JSON, XML을 사용하는데
- 데이터, 쿼리셋, 객체 등을 JSON이나 XML 등으로 변경해주는 것이 직렬화라고 한다.

### DRF에서 Serializer 사용하는 법
---
- 순서
  + DB인스턴스 생성
  + Serializing(직렬화)
  + Deserializing(비직렬화)
  + serializer.Save() (validate하는 법)

```python
# DB인스턴스 생성
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person(name="홍길동", age="20")
print(f"{person.name}, {person.age}")
# 홍길동, 20
```
- 
```python
# Serializing(직렬화)    
from rest_framework import serializers

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.CharField()

serializer = PersonSerializer(person)
serializer.data
# {'name': '홍길동', 'age': '20'}
```
```python
# Deserializing(비직렬화)
import io 
from rest_framework.parsers import JSONParser

stream = io.BytesIO(json)
data = JSONParser().parse(stream)
serializer = PersonSerializer(data=data)
serializer.is_valid()
#True
serializer.validated_data()
# {'name': '홍길동', 'age': '20'}
```

```python
# serializer.save() 
class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.CharField()
    
    def create(self, validated_data):
        return Person(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('name', instance.age)
        return instance
```
- 위와 같이 정의를 해놓으면 save()(ex-serializer.save())를 호출 시
- instance가 없으면 create
- instance가 있으면 update
- 를 자동으로 해줌