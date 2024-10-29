from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.views.generic.base import View

from cadastros.forms import CidadeForm
from cadastros.models import Cidade


class SidiaBaseView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'PROJETO SIDIA'
        return context


class CidadeList(SidiaBaseView):
    queryset = Cidade.objects.all().order_by("nome")
    context_object_name = 'cidades'
    template_name = 'cadastros/lista_cidades.html'


class CidadeDetail(DetailView):
    context_object_name = 'cidade'
    queryset = Cidade.objects.all()
    template_name = 'cadastros/detalhe_cidades.html'


class CidadeDelete(DeleteView):
    context_object_name = 'cidade'
    # queryset = Cidade.objects.all()
    model = Cidade
    template_name = 'cadastros/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeCreate(CreateView):
    model = Cidade
    # fields = ['nome', 'capital']
    form_class = CidadeForm
    template_name = 'cadastros/cadastra_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeUpdate(UpdateView, SuccessMessageMixin):
    model = Cidade
    form_class =  CidadeForm
    template_name = 'cadastros/edita_cidades.html'
    success_url = reverse_lazy('cidades-list')
    success_message = 'Cadastro atualizado com sucesso!'

# class CidadeList(View):
#
#     def get(self, request):
#         qs = Cidade.objects.all().order_by("nome")
#
#         context = {
#             'cidades': qs,
#             'titulo': 'SIDIA',
#         }
#
#         return render(request=request, template_name="cadastros/lista_cidades.html", context=context)


# def lista_cidades(request):
#     qs = Cidade.objects.all().order_by("nome")
#     context = {
#         'cidades': qs,
#         'titulo': 'SIDIA',
#     }
#
#     return render(request=request, template_name="cadastros/lista_cidades.html", context=context)


# def detalhe_cidade(request, id):
#     # id_cidade = request.GET['id_cidade']
#     # cidade = Cidade.objects.get(pk=id_cidade)
#     cidade = get_object_or_404(Cidade, pk=id)
#
#     context = {
#         'cidade': cidade
#     }
#
#     return render(request=request, template_name='cadastros/detalhe_cidades.html', context=context)


# @login_required()
# def remove_cidade(request, id):
#     if not request.user.is_authenticated:
#         raise PermissionDenied
#
#     cidade = get_object_or_404(Cidade, pk=id)
#
#     cidade.delete()
#
#     return redirect("cidades-list")


# @login_required()
# def cadastra_cidades(request):
#     if request.method == 'POST':
#         # nome = request.POST['nome']
#         # capital = request.POST['capital']
#         # Cidade.objects.create(nome=nome, capital=capital)
#
#         form = CidadeForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             return redirect('cidades-list')
#
#     else:
#         form = CidadeForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request=request, template_name='cadastros/cadastra_cidades.html', context=context)


# @login_required
# def editar_cidade(request, id):
#     # id = request.GET.get('id', None) # retorna id se tiver ou None se n tiver
#
#     # if not request.user.is_authenticated:
#     #     raise PermissionDenied
#
#     cidade_obj = get_object_or_404(Cidade, pk=id)
#     form = CidadeForm(request.POST or None, instance=cidade_obj)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('cidades-list')
#
#     context = {
#         'form': form,
#         'obj': cidade_obj
#     }
#
#     return render(request=request, template_name='cadastros/edita_cidades.html', context=context)
