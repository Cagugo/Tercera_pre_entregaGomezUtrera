from itertools import product
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Mask, SurgicalCap, CustomOrder
from .forms import MaskForm, SurgicalCapForm, CustomOrderForm, SearchForm

def index(request):
    return render(request, 'store/index.html')

def mask_list(request):
    masks = Mask.objects.all()
    return render(request, 'store/product_list.html', {'products': masks, 'type': 'Masks'})

def cap_list(request):
    caps = SurgicalCap.objects.all()
    return render(request, 'store/product_list.html', {'products': caps, 'type': 'Caps'})

def product_detail(request, product_id, product_type):
    if product_type == 'mask':
        product = get_object_or_404(Mask, id=product_id)
    else:
        product = get_object_or_404(SurgicalCap, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def custom_order(request):
    if request.method == 'POST':
        form = CustomOrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomOrderForm()
    return render(request, 'store/custom_order.html', {'form': form})

def search_products(request):
    query = request.GET.get('q')
    results = product.objects.filter(name__icontains=query)
    context = {
        'results': results,
        'result_class_name': product.__name__.lower(),
    }
    return render(request, 'store/search_results.html', context)


def add_mask(request):
    if request.method == 'POST':
        form = MaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mask_list')
    else:
        form = MaskForm()
    return render(request, 'store/add_mask.html', {'form': form})

def add_surgical_cap(request):
    if request.method == 'POST':
        form = SurgicalCapForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cap_list')
    else:
        form = SurgicalCapForm()
    return render(request, 'store/add_surgical_cap.html', {'form': form})

def add_custom_order(request):
    if request.method == 'POST':
        form = CustomOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custom_order_list')
    else:
        form = CustomOrderForm()
    return render(request, 'store/add_custom_order.html', {'form': form})
