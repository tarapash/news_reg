from django_filters import FilterSet, DateFilter
from django import forms
from .models import Post 

# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
     
     date = DateFilter(
          field_name='datetime_post',
          lookup_expr='gt',
          label='Date',
          widget=forms.DateInput(attrs={'type': 'date'})
     )

     class Meta:
     # В Meta классе мы должны указать Django модель,
     # в которой будем фильтровать записи.
          model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
          fields = {
               'heading': ['icontains'],
               'author': ['exact'],
          }

