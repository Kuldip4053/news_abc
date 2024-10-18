from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.core.paginator import Paginator


def home(request):
    return HttpResponse("hello")

def index(request):
    cid=category.objects.all()
    uid=news_detail.objects.all()
    a_tid=news_detail.objects.filter(newsposition=2).order_by("-date")[:1]
    zid=news_detail.objects.filter(newsposition=22).order_by("-date")[:1]
    b_tid=news_detail.objects.filter(newsposition=3).order_by("-date")[:1]
    c_tid=news_detail.objects.filter(newsposition=4).order_by("-date")[:1]
    d_tid=news_detail.objects.filter(newsposition=5).order_by("-date")[:1]
    t_a_tid=news_detail.objects.filter(newsposition=41).order_by("-date")[:1]
    sport_tid=news_detail.objects.filter(newsposition=30).order_by("-date")[:1]
    sport=news_detail.objects.filter(newsposition=35).order_by("-date")[:6]
    newssportnews=news_detail.objects.filter(newsposition=35).order_by("-date")[:4]
    travel_news=news_detail.objects.filter(newsposition=50)
    ent_news=news_detail.objects.filter(newsposition=40)
    lyf_news=news_detail.objects.filter(newsposition=60)
    tnews_news=news_detail.objects.filter(newsposition=51).order_by("-date")[:1]
    mornews=uid.order_by("-date")[:4]
    travelnews=travel_news.order_by("-date")[:4]
    entnews=ent_news.order_by("-date")[:4]
    lyfnews=lyf_news.order_by("-date")[:6]
    resnews=uid.order_by("-date")[:6]

    print(":")
    con={"tnews_news":tnews_news,"travelnews":travelnews,"cid":cid,
        "sport":sport,"mornews":mornews,"sport_tid":sport_tid,"newssportnews":newssportnews,"entnews":entnews,"travelnews":travelnews,
        "lyfnews":lyfnews,'uid':uid,"a_tid":a_tid,"b_tid":b_tid,"c_tid":c_tid,"d_tid":d_tid,"zid":zid,"t_a_tid":t_a_tid,"resnews":resnews
        }
    return render(request,"index.html",con)


def postpage(request):
    
    uid=news_detail.objects.all()
    cid=category.objects.all()
    uid=news_detail.objects.order_by("-date")
    
    paginator=Paginator(uid,8)
    page_number=request.GET.get("page",1)   
    uid=paginator.get_page(page_number) 
    elided=paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=1)
    con={'uid':uid,"cid":cid,"elided":elided}
    return render(request,'postpage.html',con)

def business(request):
    uid=news_detail.objects.all()
    uid=news_detail.objects.order_by("-date")
    cid=category.objects.all()
    c_id=request.GET.get("c_id")
    cn="all news"
    if c_id:
        uid=news_detail.objects.filter(newscetegory=c_id)
        uid=uid.order_by("-date")
        cn=category.objects.get(id=c_id)
    else:
        uid=news_detail.objects.all()    
    con={"uid":uid,"cid":cid,"cn":cn}        
    return render(request,"business.html",con)

def singlenews(request,id):

    uid=news_detail.objects.all()
    cid=category.objects.all()
    uid=uid.order_by("-date")
    aid=news_detail.objects.get(id=id)    
    coment_id=comment.objects.filter(post_id=aid)
    c=coment_id.count
    
    contaxt={
        "uid":uid,"aid":aid,"cid":cid,"coment_id":coment_id,"c":c}
    return render(request,"singlenews.html",contaxt)


def newscomment(request):
    if request.POST:
        postid=request.POST['postid']
        name=request.POST['name']
        email=request.POST['email']
        disc=request.POST['disc']
        print(name,postid,email,disc)
        spid=news_detail.objects.get(id=postid)
        comment.objects.create(name=name,post_id=spid,email=email,disc=disc)
    return redirect("singlenews",id=postid)
       




