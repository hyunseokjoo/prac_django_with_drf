from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# method를
# class Post_list(request):
#     # 2개 분기
#     pass
#
# class Post_detail(request):
#     # 3개 분기
#     request.method
#     pass