from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PairingMainView(TemplateView):
    template_name= 'pairing/pairing_main.html'


class PairingView(TemplateView):
    template_name= 'pairing/pairing.html'


class PairingView_cook(TemplateView):
    template_name= 'pairing/winerecipe.html'


class PairingView_beef(TemplateView):
    template_name= 'pairing/pairing_beef.html'
    


class PairingView_chiken(TemplateView):
    template_name= 'pairing/pairing_chiken.html'


class PairingView_cheese(TemplateView):
    template_name= 'pairing/pairing_cheese.html'


class PairingView_fish(TemplateView):
    template_name= 'pairing/pairing_fish.html'


class PairingView_lamb(TemplateView):
    template_name= 'pairing/pairing_lamb.html'



class PairingView_pasta(TemplateView):
    template_name= 'pairing/pairing_pasta.html'


class PairingView_pork(TemplateView):
    template_name= 'pairing/pairing_pork.html'



class PairingView_dessert(TemplateView):
    template_name= 'pairing/pairing_dessert.html'






    
