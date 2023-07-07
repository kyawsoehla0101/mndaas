from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name="frontend.en.index"),
    path('news/',views.newspage,name="frontend.en.news"),

    path('search/',views.en_searchpage,name="frontend.en_search"),
    path('statement/',views.statement,name="frontend.en.statement"),
    path('speech/',views.speech,name="frontend.en.speech"),
    path('interview/',views.interview,name="frontend.en.interview"),

    # nation url
    path('military/',views.military,name="frontend.en.military"),
    path('party/',views.party,name="frontend.en.party"),

    # alliances url
    path('northernalliance/',views.northernalliance,name="frontend.en.northernalliance"),
    path('fpncc/',views.fpncc,name="frontend.en.fpncc"),
    
    # start detail urls
    path('post/<str:slug>/',views.detail,name="frontend.en.detail"),
 ]
