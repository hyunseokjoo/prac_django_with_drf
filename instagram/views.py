from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

# generic(rest API 통합 구현)기반 APIView
# ListCreateAPIView는 list와 create api를 같이 제공하는 apiview 클래스
# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# CBV(rest API 각각 구현)기반 APIView
# class PublicPostListAPIView(APIView):
#     def get(self, request): # List용
#     #def get(self, request, pk, format=None): #detail용
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)#many는 꼭 소문자로
#         return Response(serializer.data)

# public_post_list = PublicPostListAPIView.as_view()


# FBV(rest API 각각 구현)기반 APIView
@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)  # many는 꼭 소문자로
    return Response(serializer.data)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # 들어오기 전에 먼저 dispatch내용을 적용하고 PostViewSet으로 들어온다
    def dispatch(self, request, *args, **kwargs):
        print("request:body", request.body)
        print("reuqest.POST", request.POST)
        return super().dispatch(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data) #이하 생략

    def create(self, request, *args, **kwargs):
        #is_valide()
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass

# method를
# class Post_list(request):
#     # 2개 분기
#     pass
#
# class Post_detail(request):
#     # 3개 분기
#     request.method
#     pass