'''
TODO
filter
view all cases (closed and open)
form caller, submitter
closed by
'''


from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy

from .models import Incident
from .forms import IncidentForm, MessageForm
from .location import getCoordinates
from .filters import IncidentFilter
from cms.TelegramBotAPI import tele
# Create your views here.

class MessageCreateView(LoginRequiredMixin, generic.TemplateView):

        template_name = 'cms/Message.html'
        def get(self, request, pk):
                form = MessageForm()
                return render(request, self.template_name, {'form': form})

        def post(self, request,pk):
                form = MessageForm(request.POST)
                obj = Incident.objects.get(pk=pk)
                print("form")
                if form.is_valid():
                        print("valid")
                        Message = form.cleaned_data['message']
                        obj.is_message = Message
                        postal_code = obj.location[-6:]
                        print(postal_code)
                        print(Message)
                        obj.save()
                        tele(postal_code,Message)
                        return render(request,'cms/success_social_media.html')
                print("invalid")
                return render(request, self.template_name, {'form': form})

class SuccessSMSView(TemplateView):

        template_name = 'cms/success_sms.html'

class IndexView(LoginRequiredMixin, generic.ListView):
        model = Incident

        context_object_name = 'incident_list'
        template_name = 'cms/index.html'

        conditions ={
                "severity": "severity",
                "date" : "incident_date__date"
        }

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['filter'] = IncidentFilter(self.request.GET,queryset=self.get_queryset())
                return context


class CreateIncidentView(LoginRequiredMixin, generic.TemplateView):
        template_name = 'cms/createincident.html'

        def get(self, request):
                form = IncidentForm()
                return render(request, self.template_name, {'form': form})

        def post(self, request):
                form = IncidentForm(request.POST)
                print("form")
                if form.is_valid():
                        print("valid")
                        incident = form.save(commit=False)
                        location = form.cleaned_data['street_name'] + " " + form.cleaned_data['apartment_number'] +" " + form.cleaned_data['postal_code']
                        incident.location = location
                        incident.submitter = request.user
                        incident.lat, incident.long = getCoordinates(int(form.cleaned_data['postal_code']))
                        incident.save()
                        return HttpResponseRedirect(reverse('cms:success_sms'))
                print("invalid")
                return render(request, self.template_name, {'form': form})

class DetailCase(PassRequestMixin, SuccessMessageMixin,generic.DetailView):
        template_name = 'cms/detail_case.html'
        model = Incident

        def post(self, request, pk):
                self.object = self.get_object()
                self.object.is_closed = True
                self.object.incident_closed_date = timezone.now()
                self.object.save()
                messages.info(request, "Case " + str(self.object.id) + " has been closed successfully")

                return render(request, "cms/closed_confirm.html")

class MapView(LoginRequiredMixin, generic.TemplateView):
        template_name = 'cms/view-map.html'
