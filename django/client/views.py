from .forms import LoginForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'

    def get_success_url(self):
        print("get success url")
        return reverse_lazy('home')

    def form_valid(self, form):
        print("form valid")
        response = super().form_valid(form)
        return response

    def get(self, request, *args, **kwargs):
        print("get request")
        context = self.get_context_data(**kwargs)
        if context is None:
            context = {}
        # Add custom context variables if needed
        context['form'] = LoginForm()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print("post request")
        form = LoginForm(request.POST)
        form_data = form.data
        print(form_data)
        email = form_data.get("email")
        password = form_data.get("password")
        print(email)
        print(password)

        # Override the post method to handle form submissions
        return super().post(request, *args, **kwargs)


def index(request):
    context = {}
    return render(request, 'index.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)
