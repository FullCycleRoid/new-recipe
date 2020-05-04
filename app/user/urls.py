from django.conf.urls import url

from .views import CreateUserView, CreateTokenView, ManageUserView, ListAPIUserView

app_name = 'user'


urlpatterns = [
    url(r'user-update/$', ManageUserView.as_view(), name='update'),
    url(r'user-create/$', CreateUserView.as_view(), name='create'),
    url(r'user-token/$', CreateTokenView.as_view(), name='token'),
    url(r'user-list/$', ListAPIUserView.as_view(), name='list')
]
