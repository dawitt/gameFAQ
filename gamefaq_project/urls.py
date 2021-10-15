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
from notification import views as notificationviews
from django.conf import settings
import os
from django.conf.urls.static import static
from django.conf.urls import handler400, handler403, handler404, handler500




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", postviews.HomepageView.as_view(), name="home"),
    path("logout/", authviews.logout_view, name="logout"),
    path("login/", authviews.login_view, name="login"),
    path("signup/", authviews.signup_view, name="signup"),
    path("user/<int:id>/", usersviews.UserDetailView.as_view(), name="user_detail"),
    path("users/", usersviews.all_users, name="all_users"),
    path("question-detail/<int:id>/", postviews.question_detail_view, name="question-detail"),
    path("walkthrough/<int:id>/", postviews.walkthrough_detail_view, name="walkthrough"),
    path("add-walkthrough/<int:id>", postviews.add_walkthrough, name="add_walkthrough"),
    path("console-detail/<int:id>/", apiviews.console_detail_view, name="console_detail"),
    path("console-games/<str:console>/page-<int:page>", apiviews.console_games_view, name="console_games"),
    path("game-detail/<int:id>/", apiviews.game_detail, name="game_detail"),
    path("ask-game-question/<int:id>/", postviews.ask_game_question, name="ask-game-question"),
    path("like_answer/<int:id>/", postviews.like_answer, name="like_answer"),
    path("dislike_answer/<int:id>/", postviews.dislike_answer, name="dislike_answer"),
    path("like_walkthrough/<int:id>/", postviews.like_walkthrough, name="like_walkthrough"),
    path("dislike_walkthrough/<int:id>/", postviews.dislike_walkthrough, name="dislike_walkthrough"),
    path("notifications/", notificationviews.NotificationView.as_view(), name="notifications"),
    path('searchbar/', apiviews.searchbar, name='searchbar'),
    path('searchbar/<str:search>/page-<int:page>', apiviews.searchbar_page, name='searchbarpages')

]
# STATIC URL pattern to find files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ERROR Handlers
handler404 = 'posts.views.custom_page_not_found_view'
handler500 = 'posts.views.custom_error_view'
handler403 = 'posts.views.custom_permission_denied_view'
handler400 = 'posts.views.custom_bad_request_view'