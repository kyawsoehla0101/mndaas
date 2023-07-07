from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Dashboard.models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def en_searchpage(request):
    if request.method  == 'GET':
        new_search=request.GET.get('search')
        if new_search:
            #statement component 
            last_post_statement=Post.objects.filter(category__name='Statement',user__languages='English',name__icontains=new_search)[:1]
            last_two_post_statement=Post.objects.filter(category__name='Statement',user__languages='English',name__icontains=new_search)[1:]
            #end    
            #military component
            last_post_military=Post.objects.filter(category__name='Military',user__languages='English',name__icontains=new_search)[:1]
            last_post_three_military=Post.objects.filter(category__name='Military',user__languages='English',name__icontains=new_search)[1:]
            # end

            # party conponent
            last_post_party=  Post.objects.filter(category__name='Party',user__languages='English',name__icontains=new_search)[:1]
            last_two_post_party=Post.objects.filter(category__name='Party',user__languages='English',name__icontains=new_search)[1:]
            
            context={
            'last_post_statement': last_post_statement,
            'last_two_post_statement':last_two_post_statement,
            'last_post_military':last_post_military,
            'last_post_three_military':last_post_three_military,
            'last_post_party':last_post_party,
            'last_two_post_party':last_two_post_party
        }
            return render(request,'frontend/layouts/header/en_search.html',context)
        else:
            return render(request,'frontend/layouts/header/en_search.html')
           
        
# start indexpage views
def index(request):
    latest=Post.objects.filter(user__languages='English').first()
    # nation_posts = {value:Post.objects.filter(category=key,user__languages="English")[0:3] for key, value in POST_CATEGORY} 
    statement_posts=Post.objects.filter(category="ST",user__languages='English')[0:3] 
    military_posts=Post.objects.filter(category="M",user__languages='English')[0:3] 
    party_posts=Post.objects.filter(category="P",user__languages='English')[0:3] 
    latest_three_posts=Post.objects.filter(user__languages='English')[1:4]
    context={
        'latest':latest,
        'statement_posts':statement_posts,
        # 'nation_posts':nation_posts,
        'latest_three_posts':latest_three_posts,
        'military_posts':military_posts,
        'party_posts':party_posts
        }
        
    return render(request,'frontend/en/pages/index.html',context)
# end indexpage views

# start newspage views
def newspage(request):
    last_post=Post.objects.filter(user__languages='English')[:1]
    last_two_post=Post.objects.filter(user__languages='English')[1:3]
    last_three_post=Post.objects.filter(user__languages='English')[3:7]
    right_posts=Post.objects.filter(user__languages='English')[1:7]
    all_posts=Post.objects.filter(user__languages='English')[1:10]

    context={
        'last_post':last_post,
        'last_two_post':last_two_post,
        'last_three_post':last_three_post,
        'all_posts':all_posts,
        'right_posts':right_posts
        }
    return render(request,'frontend/en/pages/news.html',context)
# end newspage views

# start statement views
def statement(request):
    latest_statement_post=Post.objects.filter(user__languages='English',category="ST").first()
    statement_others_posts=Post.objects.filter(user__languages='English',category="ST")[1:]

    context={
        'latest_statement_post':latest_statement_post,
        'statement_others_posts':statement_others_posts
        
        }
    return render(request,'frontend/en/pages/statement.html',context)
# end statement views

# start speech views
def speech(request):
  
    latest_speech_post=Post.objects.filter(user__languages='English',category="SP").first()
    speech_others_posts=Post.objects.filter(user__languages='English',category="SP")[1:]

    context={
        'latest_speech_post':latest_speech_post,
        'speech_others_posts':speech_others_posts
        
        }
    return render(request,'frontend/en/pages/speech.html',context)
# end speech views

# start interview views
def interview(request):
  
    latest_interview_post=Post.objects.filter(user__languages='English',category="IN").first()
    interview_others_posts=Post.objects.filter(user__languages='English',category="IN")[1:]

    context={
        'latest_interview_post':latest_interview_post,
        'interview_others_posts':interview_others_posts
        
        }
    return render(request,'frontend/en/pages/interview.html',context)
# end interview views




# start military in nation
def military(request):
    latest_military_post=Post.objects.filter(user__languages='English',category="M").first()
    military_others_posts=Post.objects.filter(user__languages='English',category="M")[1:]

    context={
        'latest_military_post':latest_military_post,
        'military_others_posts':military_others_posts
        
        }
    
    return render(request,'frontend/en/pages/nation/military.html',context)
# end military in nation

# start party in nation
def party(request):

    latest_party_post=Post.objects.filter(user__languages='English',category="P").first()
    party_others_posts=Post.objects.filter(user__languages='English',category="P")[1:]

    context={
        'latest_party_post':latest_party_post,
        'party_others_posts':party_others_posts
        
        }
    return render(request,'frontend/en/pages/nation/party.html',context)
# end party in nation

# start northernalliane in alliance
def northernalliance(request):

    latest_northrenalliance_post=Post.objects.filter(user__languages='English',category="NA").first()
    northrenalliance_others_posts=Post.objects.filter(user__languages='English',category="NA")[1:]

    context={
        'latest_northrenalliance_post':latest_northrenalliance_post,
        'northrenalliance_others_posts':northrenalliance_others_posts
        
        }
    return render(request,'frontend/en/pages/alliances/northernalliance.html',context)
# end northernalliane in alliance

# start fpncc in alliance
def fpncc(request):

    latest_fpncc_post=Post.objects.filter(user__languages='English',category="FPNCC").first()
    fpncc_others_posts=Post.objects.filter(user__languages='English',category="FPNCC")[1:]

    context={
        'latest_fpncc_post':latest_fpncc_post,
        'fpncc_others_posts':fpncc_others_posts
        
        }
    return render(request,'frontend/en/pages/alliances/fpncc.html',context)
# end fpncc in alliance




# start all detail 
# statement detail
def detail(request,slug):
    post=Post.objects.get(slug=slug)
    related_posts=Post.objects.filter(category=post.category,user__languages='English').exclude(slug=slug)
    
    
    context={
        'post':post,
        'related_posts':related_posts
        }
    return render(request,'frontend/en/pages/detail.html',context)
# end statement detail












