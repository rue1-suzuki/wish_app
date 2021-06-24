from django.contrib.auth.mixins import UserPassesTestMixin

from app.models import Wish


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        wish = Wish.objects.get(pk=self.kwargs['pk'])
        return self.request.user == wish.user
