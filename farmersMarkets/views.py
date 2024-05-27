from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Market, Review


def markets_list(request):
    all_markets = Market.objects.all()
    paginator = Paginator(all_markets, 10)  # Разбивка на страницы, по 10 объектов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'markets/markets_list.html', {'page_obj': page_obj})
