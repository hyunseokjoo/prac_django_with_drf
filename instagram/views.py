from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorOrReadonly
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
    permission_classes = [IsAuthenticated, IsAuthorOrReadonly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['message'] # 검색할 필드 정의 , 문자열 필드만 지정가능
    ordering_fields = ['pk'] # 지정된 필드 정렬 기중 정의, 지정안하면 모든 필드 지정
    ordering = ['pk'] # 디폴트 정렬
    
    # create하는 함수이지만 재정의 하여 사용할 수 있다
    # ip는 자동으로 들어가야하는 주소이므로 재정의 하여 save할때 자동으로 들어가게끔 정의 해주는것이 맞다.
    # 이전에 author가 로그인 되어있는지 찾는 것이 @login_required였지만, 
    # serializer에서는 authentication_classes를 사용하여 처리한다.
    def perform_create(self, serializer):
        # FIXME : 인증이 되어있다는 가정하에, author를 지정한 것
        author = self.request.user
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author, ip=ip)

    @action(detail=False, methods=['GET'])
    def public(self, request0):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        # serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fileds=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # 들어오기 전에 먼저 dispatch내용을 적용하고 PostViewSet으로 들어온다
    # def dispatch(self, request, *args, **kwargs):
    #     print("request:body", request.body)
    #     print("reuqest.POST", request.POST)
    #     return super().dispatch(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     queryset = Post.objects.all()
    #     serializer = PostSerializer(queryset, many=True)
    #     return Response(serializer.data) #이하 생략
    #
    # def create(self, request, *args, **kwargs):
    #     #is_valide()
    #     pass
    #
    # 특정 항목 검색 retrieve = 검색하다
    # def retrieve(self, request, *args, **kwargs):
    #     queryset = Post.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = PostSerializer(user)
    #     return Response(serializer.data)
    #
    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def partial_update(self, request, *args, **kwargs):
    #     pass
    #
    # def destroy(self, request, *args, **kwargs):
    #     pass

# method를
# class Post_list(request):
#     # 2개 분기
#     pass
#
# class Post_detail(request):
#     # 3개 분기
#     request.method
#     pass