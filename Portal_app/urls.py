from django.urls import path

from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, NewsSearch, IndexView

urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>/', PostDetail.as_view()),
   path('search/', NewsSearch.as_view(), name='news_search'),
   path('article/create/', PostCreate.as_view(), name='post_create'),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_edit.html'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('', IndexView.as_view()),
]