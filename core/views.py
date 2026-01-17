from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto



class IndexView(ListView):
    model = Produto
    template_name = 'index.html'
    context_object_name = 'produtos'
    queryset = Produto.objects.all()


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preço']
    success_url = reverse_lazy('index')


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preço']
    success_url = reverse_lazy('index')


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')
