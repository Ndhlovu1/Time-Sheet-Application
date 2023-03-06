from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# admin.site.register(Post)

#Add comments to be managed from the Admin Site
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name','email', 'body')


# Let's customize the way we will view our model entries in the db
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish', 'status')
    #Add a filter
    list_filter = ('status', 'created', 'publish', 'author')
    #Add a search
    search_fields = ('title', 'body')
    #Populate
    prepopulated_fields = {'slug':('title',)}
    #id fields
    raw_id_fields = ('author',)
    #A hierarchy field
    date_hierarchy = 'publish'
    #Ordering
    ordering = ('status', 'publish')


"""
#TEST IN THE PYTHON MANAGE.PY SHELL HOW TO PULL AND ADD DATA

#> from django.contrib.auth.models import User
#> from blog.models import Post
#> user = User.objects.get(username='admin')
#> post = Post(title='Another post',
     slug='another-post',
    body='Post body.',
    author=user)
#> post.save()

"""

