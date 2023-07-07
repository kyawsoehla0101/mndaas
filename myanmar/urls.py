from django.urls import path
from .import views



urlpatterns = [
    path('',views.index,name="frontend.my.index"),
    path('news/',views.newspage,name="frontend.my.news"),

    path('search/',views.en_searchpage,name="frontend.my_search"),
    path('statement/',views.statement,name="frontend.my.statement"),
    path('speech/',views.speech,name="frontend.my.speech"),
    path('interview/',views.interview,name="frontend.my.interview"),

    # nation url
    path('military/',views.military,name="frontend.my.military"),
    path('party/',views.party,name="frontend.my.party"),

    # alliances url
    path('northernalliance/',views.northernalliance,name="frontend.my.northernalliance"),
    path('fpncc/',views.fpncc,name="frontend.my.fpncc"),

    # about url
    path('leader/',views.leader,name="frontend.my.leader"),
    path('history/',views.history,name="frontend.my.history"),


     # start detail urls
    path('post/<str:slug>/',views.detail,name="frontend.my.detail"),
]