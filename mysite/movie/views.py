from django.shortcuts import render
from django.views import generic
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from .models import Dytt8


class IndexView(generic.ListView):
    template_name = 'movie/index.html'
    context_object_name = 'movie_list'
    paginate_by = 20

    def get_queryset(self):
        return Dytt8.objects.exclude(link__isnull=True).order_by('-name')


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'movie/index.html', {'error_msg': error_msg})
    movie_list = Dytt8.objects.filter(name__icontains=q)
    return render(request, 'movie/index.html', {'error_msg': error_msg,
                                                  'movie_list': movie_list})


def index(request):
    movie = Dytt8.objects.exclude(link__isnull=True)
    paginator = Paginator(movie, 20)
    page = request.GET.get('page')
    try:
        movie = paginator.page(page)
    except PageNotAnInteger:
        movie = paginator.page(1)
    except EmptyPage:
        movie = paginator.page(paginator.num_pages)
    return render(request, 'movie/index1.html', {'movie': movie})
