from django.shortcuts import render,HttpResponse
from crispyformapp.forms import CustomerForm


# Create your views here.

def customerview(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Customer details saved successfully...!</h1>")
    else:
        form = CustomerForm()
    return render(request,'home.html',{'form':form})
