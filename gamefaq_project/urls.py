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
from api import views as apiviews
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
    path("question-detail/<int:id>/", postviews.question_detail_view, name="question_detail"),
    path("walkthrough/<int:id>/", postviews.Faq_detail_view.as_view(), name="faq_detail"),
    path("add-question/", postviews.add_question, name="add_question"),
    path("add-faq/<int:id>", postviews.add_faq, name="add_faq"),
    path("console-detail/<int:id>/", apiviews.console_detail_view, name="console_detail"),
    path("console-games/<str:console>/", apiviews.console_games_view, name="console_games"),
    path("game-detail/<int:id>/", apiviews.game_detail, name="game_detail"),
    path("questions/", postviews.all_questions, name="all_questions"),
    path("ask-game-question/<int:id>/", postviews.ask_game_question, name="ask-game-question"),




    
]

# urlpatterns + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 