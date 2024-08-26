from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse




class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rank_post'))
        post_rat = 0
        post_rat +=  postRat.get('postRating')

        commentRat = self.author_user.comment_set.aggregate(commentRating=Sum('rank_comment'))
        com_rat = 0
        com_rat += commentRat.get('commentRating')

        self.rating_author = post_rat*3 + com_rat
        self.save()



class Category(models.Model):
    name = models.CharField(max_length = 255, unique = True)



class Post(models.Model):

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )

    CategoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE) #PostCategory
    author = models.ForeignKey(Author,  on_delete=models.CASCADE)
    datetime_post = models.DateTimeField(auto_now_add = True)
    heading = models.CharField(max_length = 255)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    text = models.TextField()
    rank_post = models.IntegerField(default=0)

    def preview(self):
        return self.text[0:123] + '...'

    def like(self):
        self.rank_post += 1
        self.save()

    def dislike(self):
        self.rank_post -= 1
        self.save()

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

class PostCategory(models.Model): #TopicPost
    post =  models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:10]}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length = 255)
    datetime_comment = models.DateTimeField(auto_now_add = True)
    rank_comment = models.IntegerField(default=0)
    def like(self):
        self.rank_comment += 1
        self.save()

    def dislike(self):
        self.rank_comment -= 1
        self.save()


