from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'BLOG_POSTS/POST_FORM.html')