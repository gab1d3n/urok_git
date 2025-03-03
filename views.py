from django.shortcuts import render, redirect
from .forms import ProductFormSet

def product_view(request):
    if request.method == "POST":
        formset = ProductFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('success_page') 
    else:
        formset = ProductFormSet()

    return render(request, 'your_app/product_form.html', {'formset': formset})

def success_page(request):
    return render(request, 'your_app/success.html')
