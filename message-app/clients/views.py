from django.shortcuts import render
from .models import Client
from .forms import CreateClientForm
from django.views.generic import ListView, CreateView
# Create your views here.
from django.urls import reverse_lazy

class HomePageView(ListView):
    template_name = "index.html"
    context_object_name = "clients"
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateClientForm()
        return context

    # def post(self, request, *args, **kwargs):
    #     Client.objects.create()

    # def get(self. request, *args, **kwargs):
    #     clients = Client.objects.get()
    #     return render(request, self.template_name, {

    #     })

class CreateClientView(CreateView):
    model = Client
    form_class = CreateClientForm
    # template_name = 'notes/create_note.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)