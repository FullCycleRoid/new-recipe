from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import TagRetrieveUpdateAPIView, TagListAPIView, \
     TagCreateAPIView, RecipeViewSet, IngredientsViewSet

app_name = 'recipe'

router = DefaultRouter()
router.register(r'ingredients', IngredientsViewSet, basename='ingredients')
router.register(r'recipe', RecipeViewSet, basename='recipe')

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'tag-list/$', TagListAPIView.as_view(), name='tag-list'),
    url(r'new-tag/$', TagCreateAPIView.as_view(), name='tag-create'),
    url(r'tag/(?P<name>[-\w]+)/$', TagRetrieveUpdateAPIView.as_view(), name='tag-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
