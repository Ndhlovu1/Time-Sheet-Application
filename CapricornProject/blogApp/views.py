from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail


"""Django Template Language
    Template Tags = Control Rendering of the template with - #{% tag %}
    Template Variables = Get replaced with values when the template is rendered - #{ variable }
    Template Filters = Allow variable modification for display - #{{ variable|filter }}
"""

#A class based list view
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# A view is a django class/function that receives a web request and returns a web response

def list_posts(req):
    
    object_list = Post.published.all()
    paginator = Paginator(object_list,3) # 3 Posts Per Page
    page = req.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)#SHould there be no numbers load first page

    except EmptyPage:
        #Page Out of range, load last page
        posts = paginator.page(paginator.num_pages)

    return render(req, 'blog/post/list.html', {'page':page, 'posts':posts})



#single post display
def single_post(request, year,month,day,post):

    post = get_object_or_404(Post, 
        slug=post,
        status='published',
        publish__year = year,
        publish__month = month,
        publish__day=day
    )

    #List of active Comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        #Commented Post
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # ... Add db
            new_comment = comment_form.save(commit=False)
            #Assign it to a post
            new_comment.post = post
            #Save to db
            new_comment.save()
            
    else:
        comment_form = CommentForm()


    return render(request, 'blog/post/detail.html',{
        'post':post,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form
        })


#Send an Email View
def share_post(request, post_id):

    post = get_object_or_404(Post, 
    id=post_id, 
    status='published')

    sent = False

    if request.method == 'POST':
        #Successfull submission

        form = EmailPostForm(request.POST)

        if form.is_valid():
            #Validation was successfull

            cd = form.cleaned_data
                       
            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = f"{ cd['name'] } has suggested this blog for you - { post.title }"

            message = f"Read { post.title } at { post_url } -- { cd['name'] } comments: { cd['comments'] }"

            send_mail(subject,message, 'sltnaphx@gmail.com',[ cd['to'] ])

            sent = True


    else:
        form = EmailPostForm()
         
    return render(
            request, 
            'blog/post/share.html', {
                'post':post, 
                'form':form, 
                'sent':sent})
        
# Sending EMAILS - REMEMBER THE BELOW

"""
        EMAIL_HOST: THE SMTP SERVER HOST, THE DEFAULT IS LOCALHOST
        EMAIL_PORT: THE SMTP PORT, THE DEFAULT IS 25
        EMAIL_HOST_USER: THE SMTP USERNAME FOR THE SERVER
        EMAIL_HOST_PASSWORD: THE SMTP PASSWORD FOR THE SERVER
        EMAIL_USE_TLS: OPTION TO USE Transport Layer Security(TLS) secure connection
        EMAIL_USE_SSL: OPTION TO USE AN IMPLICIT TLS SECURE CONNECTION
        
        # If you can't use the smtp server you can write have django write the emails to the console in the settings.py
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        #The above will push all emails to the console

        #Google how to setup an Ubuntu Email Server
        If you don't have an email server but would like to use the gmail
        
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = 'backend@gmail.com'
        EMAIL_HOST_PASSWORD = 'Not My Actual Phrase'
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True

        TO TEST - python3 manage.py shell
        from django.core.email import send_mail
        send_mail('Hello From Django', 'This is amazing stuff, the possibilities are endless.', 'backend@gmail.com',['backend@gmail.com], fail_silently=False)

        When you get 1, it means it worked!

"""

        #Iterating through each field in a form field
"""
        {% for field in form %}
            <div>
            {{ field.errors }}
            {{ field.label_tag }} {{ field }}
            </div>
        {% endfor %}
        
"""
    


