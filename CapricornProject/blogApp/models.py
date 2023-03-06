from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Create your own custom Model Manager to pull 
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(
            PublishedManager, self
        ).get_queryset().filter(status='published')
        
#A post Table
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft' , 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    #This method will be used to link to specific postsin the templates
    def get_absolute_url(self):
        return reverse(
            'blogApp:single_post',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )


    class Meta:
        ordering = ('-publish',)

    objects = models.Manager()
    published = PublishedManager() #Call only the published blog articles

    #This is the default human readable representation of our table db
    def __str__(self):
        return self.title



    #Once this is all done
    """
    RUN THE DATABASE MIGRATION(HOPEFULLY YOUR VIRTUAL ENVIRONMENT IS ACTIVE)
        python / python3 manage.py makemigrations
        python / python3 manage.py migrate

        USE ONLY ONE python on the above example, depending on the total amounts of python you have

        TO VIEW THE MIGRATION IN SQL TYPE THE COMMANDS BELOW
            python / python3 manage.py sqlmigrate blogApp 0001
    
    """

    #THIS IS THE FIRST PART
    """
    FROM THERE VISIT THE ADMIN FILE TO SEE THE CHANGES THAT HAVE BEEN MADE
    THEN IN THE TERMINAL TYPE
    python / python3 manage.py createsuperuser
    ## Answer them accordingly
    User - Admin@backendguru
    Password - Admin987!

    ## VISIT THE localhost:8000/admin
    
    """

#A class to keep the Comments made on the posts
class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    name = models.CharField(max_length=80)

    email = models.EmailField()

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)


    def __str__(self):
        return f"Comment by {self.name} on {self.post}"





