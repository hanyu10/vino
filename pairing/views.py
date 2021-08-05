from django.views.generic import FormView
from pairing.forms import Pairingform

# Create your views here.
 
def PairingView(FormView):
    template_name= 'pairing/index.html'
    form_class = Pairingform
    success_url = '.'

    def post(self, requet, *args, **kwargs):
        return super().post(requet, *args, **kwargs)