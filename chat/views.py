from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class RoomView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/room.html'

    def get_context_data(self, **kwargs):
        self.extra_context = {'room_name': kwargs['room_name']}
        return super().get_context_data(**kwargs)
