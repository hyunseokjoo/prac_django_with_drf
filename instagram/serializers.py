from rest_framework.serializers import ModelSerializer
from .models import Post

# 보통 http api 통신을 할 때 json이나 xml을 이용하여 진행하게 되는데 요즘에는 용량이 작은 json을 주로 사용한다
# 또한 api 통신에서 json 파일을 db에 인스턴스 저장을 하거나 db에 있는 인스턴스를 json파일로 변환을 해서 요청 응답을 하게 되는데
# Serializer는 이것을 처리해주는 용도이다
# serializer = db -> json 변환
# deserializer = json -> db 변환환
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'