from django.conf.urls import url

from .views import DashBoardView

urlpatterns = [
    url(r'^$', DashBoardView.as_view(), name='dashboard'),
    # url(r'^account/login/$', LoginView.as_view(), name='login'),
    url(r'^user/list/$', WikiListView.as_view(), name='wiki_list'),

]
