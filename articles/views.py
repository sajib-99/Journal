from django.shortcuts import render, HttpResponse
from articles.models import Post

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

# Create your views here.
def articlesHome(request):
    allPosts= Post.objects.all().order_by('-timeStamp')

    paginator = Paginator(allPosts, 3)   
    page_num = request.GET.get('page',1)
    page = paginator.page(page_num)
    
    context={'items': page}
    
    return render(request,'articles.html', context)

@login_required(login_url='/login_register')
def articlesPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request,'articlespost.html',  context)




