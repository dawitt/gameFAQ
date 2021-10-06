"""gamefaq_project URL Configuration

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
# from users import views
from authentication import views as authviews
from posts import views as postviews
from users import views as usersviews
from django.conf import settings
import os
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", postviews.homepage_view, name="home"),
    path("logout/", authviews.logout_view, name="logout"),
    path("login/", authviews.login_view, name="login"),
    path("signup/", authviews.signup_view, name="signup"),
    path("user/<int:id>/", usersviews.User_detail_view.as_view(), name="user_detail"),
    path("comments/<int:id>/", postviews.Comment_detail_view.as_view(), name="comment_detail"),
    path("questions/<int:id>/", postviews.Question_detail_view.as_view(), name="question_detail"),
    path("faqs/<int:id>/", postviews.Faq_detail_view.as_view(), name="faq_detail"),
    path("add-comment/", postviews.add_comment, name="add_comment"),
    
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT) 