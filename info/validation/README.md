# Validation

### Validation이란?
---
- update, create 등을 진행 할 때 필드에 맞는 값을 넣어줘야하기 때문에 검증 작업이 필요하다
- DRF serializer에서는 validate하는 방법이 여러가지 존재 한다.

- 순서
  + Field-level validation 구현하기
  + Object-level validation 구현하기
  + validator로 만들어 validation 구현하기
  + Meta를 이용하여 validation 구현하기

- Field-level validation 구현하기
```python
from rest_framework import serializers

class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self, value):
        if 'django' not in value.lower:
            raise serializers.ValidationError("타이틀에는 django의 문구가 들어가야합니다.")
        return value
```
- Object-level validation 구현하기
```python
from rest_framework import serializers

class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()
    
    def validate(self, data):
        if data['start'] > data['finish']:
            raise serializers.ValidationError("오류")
        return data
```

- validator로 만들어 validation 구현하기
```python
from rest_framework import serializers

def check_person(value):
    if value == "남성" or value == "여성":
        raise serializers.ValidationError("사람이 아닙니다.")
  
class PersonSerializer(serializers.Serializer):
    gender = serializers.CharField(validators=[check_person])
```

- Meta를 이용하여 validation 구현하기
```python
class EventSerializer(serializers.Serializer):
    name = serializers.CharField()
    room_number = serializers.IntegerField(choices=[101, 102, 103, 201])
    date = serializers.DateField()

    class Meta:
        # Each room only has one event per day.
        validators = [
            UniqueTogetherValidator(
                queryset=Event.objects.all(),
                fields=['room_number', 'date']
            )
        ]
```

- [참조](https://www.lostcatbox.com/2021/01/19/django-serializer/)