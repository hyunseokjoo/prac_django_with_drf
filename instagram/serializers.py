from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

# 보통 http api 통신을 할 때 json이나 xml을 이용하여 진행하게 되는데 요즘에는 용량이 작은 json을 주로 사용한다
# 또한 api 통신에서 json 파일을 db에 인스턴스 저장을 하거나 db에 있는 인스턴스를 json파일로 변환을 해서 요청 응답을 하게 되는데
# Serializer는 이것을 처리해주는 용도이다
# serializer = db -> json 변환
# deserializer = json -> db 변환환

#중첩 serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']



class PostSerializer(serializers.ModelSerializer):
    #username = serializers.ReadOnlyField(source='author.username') # attr serializer
    #author_email = serializers.ReadOnlyField(source='author.email')

    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = [
            'pk',
            'author', # Post 모델에는 username이라는 항목이 없는데 위에 attr로 지정해 사용가능하다
            #'username',
            #'email',
            'message',
            'created_at',
            'updated_at',
        ]