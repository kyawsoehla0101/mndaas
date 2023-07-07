from django.shortcuts import render,redirect
from .models import*

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
# start loginpage views
def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username,password=password)
        except:
            messages.error(request, 'Sorry! User Does Not Exists')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboardpage')
    return render(request,'accounts/login.html')
#  end loginpage views

# start logout page views
def logoutpageviews(request):
    logout (request)
    return redirect('loginpage')
# end logout page views
# start dashboard page views
def dashboardpageviews(request):
    all_posts=Post.objects.all()
    
    
    context={
        'all_posts':all_posts
    }
    

    return render(request,'backend/pages/dashboard.html',context)
# start all create pages

# start post create page views
def postcreatepageviews(request):
  

    if request.method == 'POST':
        title=request.POST.get('name')
        category=request.POST.get('category')
        text=request.POST.get('discription')
        image=request.FILES.get('image')

        Post.objects.create(
            name=title,
            category_id=category,
            discription=text,
            images=image,
            user=request.user
            )
        if 'saveandanother' in request.POST:
            return redirect('postcreatepage')
        else:
            return redirect('dashboardpage')


    context={
        'category':category
        }
    
    return render(request,'backend/CRUD/postcreate.html',context)
# end post create page views

# start announcements create page
def announcementcreatepage(request):
    announcement_category=AnnoumcementCategory.objects.all()
    if request.method == 'POST':
        title=request.POST.get('name')
        category=request.POST.get('category')
        text=request.POST.get('discription')
        image=request.FILES.get('image')

        Post.objects.create(
            name=title,
            category_id=category,
            discription=text,
            images=image,
            user=request.user
            )
        if 'saveandanother' in request.POST:
            return redirect('announcementcreatepage')
        else:
            return redirect('dashboardpage')
    context={
        'announcement_category':announcement_category
        }
    return render(request,'backend/CRUD/announcementcreate.html',context)
# end announcements create page

# start alliances create page
def alliancecreatepageviews(request):
    category=Category.objects.all()
    alliance_category=AllianceCategory.objects.all()
    if request.method == 'POST':
        title=request.POST.get('name')
        category=request.POST.get('category')
        alliance=request.POST.get('alliancecategory')
        text=request.POST.get('discription')
        image=request.FILES.get('image')

        Alliance.objects.create(
            name=title,
            category_id=category,
            alliancecategory_id=alliance,
            discription=text,
            images=image,
            user=request.user
            )
        if 'saveandanother' in request.POST:
            return redirect('alliancecreatepage')
        else:
            return redirect('dashboardpage')
    context={
        'alliance_category':alliance_category,
        'category':category
        }
    return render(request,'backend/CRUD/alliancescreate.html',context)
# end alliances create page

# start category create page views
def categorycreatepageviews(request):
    allcategory=Category.objects.all
    if request.method =='POST':
        categoryname=request.POST.get('category')
        Category.objects.create(
            name=categoryname

        )
        return redirect('categorycreatepage')
    context={
        'allcategory':allcategory
    }

    return render(request,'backend/CRUD/category/categorycreate.html',context)
# end post category page views



# start category detail page views
def categoryallpageviews(request):
    return render(request,'backend/CURD/category/categoryall.html')
# end category detail page views
# end all create pages

# start delete post page views
def postdeletepageviews(request,pk):
    post=Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboardpage')
    return render(request,'backend/CRUD/postdelete.html')
# end delete post page views

# start all pages update
# start update post page views
def postupdatepageviews(request,slug):
    postupdate=Post.objects.get(slug=slug)
    category=Category.objects.all()
    if request.method == 'POST':
        if request.FILES.get('image'):
            title=request.POST.get('name')
            category=request.POST.get('category')
            text=request.POST.get('discription')
            image=request.FILES.get('image')

            postupdate.name=title
            postupdate.category_id=category
            postupdate.discription=text
            postupdate.images=image

            postupdate.save()
            if 'postupdate' in request.POST:
                return redirect('dashboardpage')
            
        title=request.POST.get('name')
        category=request.POST.get('category')
        text=request.POST.get('discription')
        # image=request.FILES.get('image')

        postupdate.name=title
        postupdate.category_id=category
        postupdate.discription=text
        #  postupdate.images=image
        postupdate.save()
        return redirect('dashboardpage')
    return render(request,'backend/CRUD/postupdate.html',{'postupdate':postupdate,'category':category})

        
        
# end update post page views

# start update statement page views
def statementupdatepageviews(request,pk):
    postupdate=Post.objects.get(id=pk)
    category=Category.objects.all()
    if request.method == 'POST':
        if request.FILES.get('image'):
            title=request.POST.get('name')
            category=request.POST.get('category')
            text=request.POST.get('discription')
            image=request.FILES.get('image')

            postupdate.name=title
            postupdate.category_id=category
            postupdate.discription=text
            postupdate.images=image

            postupdate.save()
            if 'postupdate' in request.POST:
                return redirect('statementpage')
            
        title=request.POST.get('name')
        category=request.POST.get('category')
        text=request.POST.get('discription')
        # image=request.FILES.get('image')

        postupdate.name=title
        postupdate.category_id=category
        postupdate.discription=text
        #  postupdate.images=image
        postupdate.save()
        return redirect('statementpage')
    return render(request,'backend/CRUD/statementupdate.html',{'postupdate':postupdate,'category':category})
# end update statement post page views

# start statement page views
def statementpageviews(request):
    
    statement_posts=Post.objects.filter(category__name='Statement')
    context={
        'statement_posts':statement_posts
    }
    return render(request,'backend/pages/statement.html',context)
# end statement page views

# start military page views
def militarypageviews(request):
    military_posts=Post.objects.filter(category__name='Military')
    context={
        'military_posts':military_posts
    }
    return render(request,'backend/pages/military.html',context)
# end military page views

# start party page views
def partypageviews(request):
    party_posts=Post.objects.filter(category__name='Party')
    context={
        'party_posts':party_posts
    }
    return render(request,'backend/pages/party.html',context)
# end party page views




# post detail page views
def postdetailpageviews(request,slug):
    all_posts=Post.objects.all()
    detail_post=Post.objects.get(slug=slug)
    
    context={
        'all_posts':all_posts,
        'detail_post':detail_post
     
        }
    return render(request,'backend/CRUD/postdetail.html',context)
# post detail page views

