from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

# ListCreateAPIView는 list와 create api를 같이 제공하는 apiview 클래스
class PublicPostListApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all() #filter(is_public=True)
    serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        print("request:body", request.body)
        print("reuqest.POST", request.POST)
        return super().dispatch(request, *args, **kwargs)

# method를
# class Post_list(request):
#     # 2개 분기
#     pass
#
# class Post_detail(request):
#     # 3개 분기
#     request.method
#     pass