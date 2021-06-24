from app.forms import MyUserChangeForm, MyUserCreationForm
from django.contrib.auth import authenticate, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic


class Create(generic.CreateView):
    template_name = 'app/user/create.html'
    model = get_user_model()
    form_class = MyUserCreationForm
    success_url = reverse_lazy('app:todo_list')

    def form_valid(self, form):
        response = super().form_valid(form)

        un = form.cleaned_data.get('username')
        pw = form.cleaned_data.get('password1')
        user = authenticate(username=un, password=pw)
        login(self.request, user)
        return response


class List(generic.ListView):
    template_name = 'app/user/list.html'
    model = get_user_model()


class Detail(generic.DetailView):
    template_name = 'app/user/detail.html'
    model = get_user_model()


class Update(generic.UpdateView):
    template_name = 'app/user/update.html'
    model = get_user_model()
    form_class = MyUserChangeForm
    success_url = reverse_lazy('app:todo_list')


class Delete(generic.DeleteView):
    template_name = 'app/user/delete.html'
    model = get_user_model()
    success_url = reverse_lazy('app:todo_list')
