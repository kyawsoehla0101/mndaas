from django.urls import path
from .import views

urlpatterns=[
    # start dashboard urls
    path('dashboard/',views.dashboardpageviews,name="dashboardpage"),
    path('post/create/',views.postcreatepageviews,name='postcreatepage'),
    path('announcement/create/',views.announcementcreatepage,name='announcementcreatepage'),
    path('alliance/create/',views.alliancecreatepageviews,name='alliancecreatepage'),




    path('statement/',views.statementpageviews,name="statementpage"),
    path('military/',views.militarypageviews,name="militarypage"),
    path('party/',views.partypageviews,name="partypage"),
    path('category/create/',views.categorycreatepageviews,name="categorycreatepage"),
    path('categories/',views.categoryallpageviews,name="allcategorypage"),


    # dashboard detail urls 

    path('post/<str:slug>/',views.postdetailpageviews,name="postdetailpage"),
    path('post/delete/<str:pk>/',views.postdeletepageviews,name="postdeletepage"),

    path('post/<str:pk>/',views.postdetailpageviews,name="postdetailpage"),
    path('post/delete/<str:pk>/',views.postdeletepageviews,name="postdeletepage"),
    path('post/change/<str:slug>/',views.postupdatepageviews,name="postupdatepage"),

    path('statement/change/<str:pk>/',views.statementupdatepageviews,name="statementupdatepage"),

    # accounts and admin urls
    path('login/',views.loginpage,name="loginpage"),
    path('logout/',views.logoutpageviews,name="logoutpage"),
 
    
]