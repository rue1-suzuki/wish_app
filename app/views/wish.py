from app.mixins import OnlyYouMixin
from app.models import Wish
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone


class Create(LoginRequiredMixin, generic.CreateView):
    template_name = 'app/wish/create.html'
    model = Wish
    success_url = reverse_lazy('app:wish_list')
    fields = ['title', 'price', 'count',
              'expected_buy_date', 'shopname', 'priority', ]

    def get_form(self):
        datetime_widget = forms.DateTimeInput(
            attrs={'type': 'date', }
        )

        form = super().get_form()
        form.fields['expected_buy_date'].widget = datetime_widget
        form.fields['expected_buy_date'].input_formats = ['%Y-%m-%d']
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'app/wish/list.html'
    model = Wish

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(user=self.request.user)
        return query


class Detail(OnlyYouMixin, generic.DetailView):
    template_name = 'app/wish/detail.html'
    model = Wish


class Update(OnlyYouMixin, generic.UpdateView):
    template_name = 'app/wish/update.html'
    model = Wish
    success_url = reverse_lazy('app:wish_list')
    fields = ['title', 'price', 'count',
              'expected_buy_date', 'shopname', 'priority', ]

    def get_form(self):
        datetime_widget = forms.DateTimeInput(
            attrs={'type': 'date', }
        )

        form = super().get_form()
        form.fields['expected_buy_date'].widget = datetime_widget
        form.fields['expected_buy_date'].input_formats = ['%Y-%m-%d']
        return form


class Delete(OnlyYouMixin, generic.DeleteView):
    template_name = 'app/wish/delete.html'
    model = Wish
    success_url = reverse_lazy('app:wish_list')


class SwitchStatus(OnlyYouMixin, generic.UpdateView):
    model = Wish
    fields = ['buy_date', ]

    def form_valid(self, form):
        wish = Wish.objects.get(pk=self.kwargs['pk'])
        if wish.buy_date:
            form.instance.buy_date = None
        else:
            form.instance.buy_date = timezone.now().date()
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        wish = Wish.objects.get(pk=self.kwargs['pk'])
        url = self.request.META['HTTP_REFERER']
        return f'{url}#wish{wish.pk}_{wish.title}'
