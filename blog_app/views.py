# coding: utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from blog_app.models import Article
from django.http import Http404
from django.db.models import Q


def index(request):
    article_list = Article.objects.all().order_by('-upload_time')
    print '*************look here******************'
    print article_list
    print '****************************************'
    article_list_cut = article_list[0:3]
    return render_to_response('index.html', {'article_list_cut': article_list_cut,
                                             })


def category(request, dynamic_category_url=None):  # 缺省到None然后可以传送默认页面
    if not dynamic_category_url:
        return render_to_response('category.html', {'category': None, 'position_test': dynamic_category_url})
        # 没有动态目录url时,显示的应该是默认的网页
    else:
        category = dynamic_category_url
        category_cap = dynamic_category_url.capitalize()
        category_list = Article.objects.filter(Q(category=category) | Q(category=category_cap))
        if not category_list:  # 在url中含有参数,但是没有对应标签的时候
            return render_to_response('category.html',
                                      {'category': category_list,
                                       'alt_content': True,
                                       'position_test': 'test1'})
        else:
            return render_to_response('category.html',
                                      {'category': category_list,
                                       'alt_content': False,
                                       'tag': category,  # 你查询的标签种类
                                       'position_test': 'test2'})


def article(request, dynamic_article_url=None):
    if not dynamic_article_url:
        return render_to_response('category.html', {'category':None})
    try:
        article = Article.objects.get(title=dynamic_article_url)
        return render_to_response('articles.html', {'article': article})
    except Article.DoesNotExist:
        return render_to_response('404.html')   # 这里在后期可以自己返回404页面



def about_me(request):
    return render_to_response('about_me.html')


def four_zero_four(request):
    return render_to_response('404.html')


def comment(request):
    pass





# Create your views here.
