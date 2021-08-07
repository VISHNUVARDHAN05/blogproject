from django.shortcuts import render
from django.http import HttpResponse
from .models import blog,category
def home_view(request):
    blog_obj=blog.objects.all()
    print(blog_obj)
    context = {
        'blog_obj':blog_obj
    }
    return render(request,'home.html',context)
def category_view(request):
    try:
        cat_obj = category.objects.all()
        print(cat_obj)
        context={
            'cat_obj':cat_obj,
        }
        return render(request,'categories.html',context)
    except:
        return HttpResponse('<h2>Page Not Found...</h2>')

def detailed_view(request,category,title):
    try:
        get_blog=blog.objects.get(category=category,title=title)
        context = {
            'get_blog':get_blog,
        }
        print(get_blog)
        return render(request, 'details.html', context)

    except:
        #return render(request, 'details.html', context)
        return HttpResponse('<h2>Page Not Found...</h2>')
def list_all_view(request,category):
    print(blog.objects.all())
    try:
        all_cat_obj=blog.objects.filter(category=category)
        if len(all_cat_obj)>0:
            context = {
                'all_cat_obj':all_cat_obj,
            }
            return render(request,'all_cat_objects.html',context)
        else:
            print('kfjkdbibsdifb')
            return HttpResponse('<h2>Page Not Found...</h2>')
    except:
        pass

