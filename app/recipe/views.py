from rest_framework import permissions, authentication, status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer, RecipeImageSerializer
from core.models import Tag, Ingredient, Recipe


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class APIRootView(APIView):

    def get(self, request):
        data = {
            'user-list': reverse('user:list', request=request),
            'user-create': reverse('user:create', request=request),
            'user-update': reverse('user:update', request=request),
            'user-token': reverse('user:token', request=request),
            'tag-list': reverse('recipe:all-tags', request=request),
            'tag-create': reverse('recipe:new-tag', request=request),
        }
        return Response(data)


class TagRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated & IsOwnerOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'name'


class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreateAPIView(CreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class IngredientsViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipeSerializer
        elif self.action == 'upload-image':
            return RecipeImageSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(detail=True, methods=['POST'], url_path='upload-image')
    def upload_image(self):
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
