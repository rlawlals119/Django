from django.shortcuts import render,redirect,get_object_or_404   # 장고 shortcuts에서 제공하는 get_object_or_404 함수를 가져옴
from django.utils import timezone
from .models import Blog    # models.py 의 Blog DB를 받아옴


# Create your views here.
def home(request):
    blogs = Blog.objects.all()  #Blog 테이블에 있는 객체들을 모두 blogs에 저장
    return render(request, 'home.html', {'blogs':blogs})    # home.html과 함께 blogs라는 키값에 담겨져있는 bolgs를 보냄
# request를 받아서 home.html 로 렌더링 해주는 함수

def detail(request, id):    # id 값이 있는 Blog를 가져오거나 404페이지를 띄워라
    blog = get_object_or_404(Blog, pk = id)    # 서버에 존재하지 않는 페이지를 요청하면 404 페이지를 띄움, pk=Primary Key(기본키)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)  # 작성한 글을 detail.html로

def edit(request,id):
    edit_blog = Blog.objects.get(id=id) # get을 사용하여 하나의 object만 가져옴
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request,id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')