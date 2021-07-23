"""lionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import *    # blog 앱에 있는 views.py의 모든 함수를 가져온다는 뜻, *가 모든걸 가져오는 건가 봄

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"), # 첫번째 인자는 경로, 두번째 인자는 views.py에서 만든 함수 이름, 세번째 인자는 접근가능한 이름
    path('<str:id>',detail, name="detail"),    # Path-converter # <str:id>에서 str은 자료형이고 id는 매개변수 이름, id값에 따라 페이지가 다르게 보임
    path('new/',new, name="new"),
    path('create/',create,name="create"),
    path('edit/<str:id>',edit,name="edit"),
    path('update/<str:id>',update,name="update"),
    path('delete/<str:id>',delete,name="delete"),
]
# views.py에 함수가 생길때마다 urls.py에 path를 추가해줘야 된다고 생각하면 됨