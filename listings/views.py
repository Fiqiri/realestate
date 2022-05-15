from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from .models import Listing
from .choices import price_choices, bedroom_choices, city_choices, shitje_qera_choices
from django.db.models import Q


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings,
        'city_choices': city_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'shitje_qera_choices': shitje_qera_choices,
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(description__icontains=keywords) | Q(title__icontains=keywords))

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

        # Zona
    if 'zona' in request.GET:
        zona = request.GET['zona']
        if zona:
            queryset_list = queryset_list.filter(zona__icontains=zona)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)


    # Shitje/Qera
    if 'shitje_qera' in request.GET:
        shitje_qera = request.GET['shitje_qera']
        if shitje_qera:
            queryset_list = queryset_list.filter(shitje_qera__iexact=shitje_qera)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    context = {
        'city_choices': city_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'shitje_qera_choices': shitje_qera_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
