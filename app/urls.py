from django.urls import path
from django.views import generic

from app.views import wish, user


class Index(generic.TemplateView):
    template_name = 'app/index.html'


app_name = 'app'

urlpatterns = [
    path('user/', user.List.as_view(), name='user_list'),
    path('user/add/', user.Create.as_view(), name='user_create'),
    path('user/<int:pk>/', user.Detail.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', user.Update.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', user.Delete.as_view(), name='user_delete'),

    path('wish/', wish.List.as_view(), name='wish_list'),
    path('wish/add/', wish.Create.as_view(), name='wish_create'),
    path('wish/<int:pk>/', wish.Detail.as_view(), name='wish_detail'),
    path('wish/<int:pk>/update/', wish.Update.as_view(), name='wish_update'),
    path('wish/<int:pk>/delete/', wish.Delete.as_view(), name='wish_delete'),

    path(
        'wish/<int:pk>/switch/is_buy/',
        wish.SwitchStatus.as_view(),
        name='wish_switch_is_buy'
    ),
]
