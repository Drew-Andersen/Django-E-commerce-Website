from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'shop_app/shop_index.html'

class TestView(TemplateView):
    template_name = 'shop_app/test.html'

class UserLoginView(View):
    def get(self, request):
        return render(request, 'shop_app/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Account is not active.')
        else:
            return HttpResponse('Invalid login details supplied!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    
class RegisterView(View):
    def get(self, request):
        user_form = UserForm()
        return render(request, 'shop_app/register.html', 
                      {'user_form': user_form, 
                       'registered': False})

    def post(self, request):
        registered = False
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)  
            user.set_password(user.password)  
            user.save()  
            registered = True
        else:
            print(user_form.errors)
        
        if registered:
            return redirect('login')

        return render(request, 'shop_app/register.html', 
                      {'user_form': user_form, 
                       'registered': registered})