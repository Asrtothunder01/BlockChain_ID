"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView,SpectacularAPIView, SpectacularSwaggerView
from college.views import CollegeCreateView
from department.views import DepartmentListView
from course.views import CourseListView
from question.views import QuestionListView
from discussion.views import DiscussionListView
from post.views import PostListView
from answer.views import AnswerListView
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path ('account/', include ('account.urls')),
    
    path('answer/', AnswerListView.as_view(), name = 'Answer'),
    
    path ('post/', PostListView.as_view(),name = 'Post'),
    
    path('discuss/', DiscussionListView.as_view(), name = 'Dicussion'),
    
    path('depart/',DepartmentListView.as_view(), name  = 'depart'),
    path ('course/', CourseListView.as_view(), name= 'course'),
    
    path ('college/',CollegeCreateView.as_view(), name = 'college'),
    
    path('quest/', QuestionListView.as_view(), name= 'question'),
    
    path('schema/', SpectacularAPIView.as_view(), name = 'schema'),
    
    path('swagger/', SpectacularSwaggerView.as_view(url_name = 'schema'), name = 'swagger_ui',)
]
