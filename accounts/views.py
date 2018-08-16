from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def register(request):
    return render(request, "accounts/register.html")