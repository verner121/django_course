from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from client.forms import ClientForm, MessageForm, MailingForm

from client.models import Client, Message, Mailing


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client:client_list')


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'
    context_object_name = 'client'
    success_url = reverse_lazy('client:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/client_delete.html'
    success_url = reverse_lazy('client:client_list')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'client/message_form.html'
    success_url = reverse_lazy('client:message_list')


class  MessageListView(ListView):
    model = Message
    template_name = 'client/message_list.html'
    context_object_name = 'messages'


class  MessageDetailView(DetailView):
    model = Message
    template_name = 'client/message_detail.html'
    context_object_name = 'message'
    success_url = reverse_lazy('client:message_list')


class  MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'client/message_form.html'
    success_url = reverse_lazy('client:message_list')


class  MessageDeleteView(DeleteView):
    model = Message
    template_name = 'client/message_delete.html'
    success_url = reverse_lazy('client:message_list')


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'client/mailing_form.html'
    success_url = reverse_lazy('client:mailing_list')


class  MailingListView(ListView):
    model = Mailing
    template_name = 'client/mailing_list.html'
    context_object_name = 'mailings'


class  MailingDetailView(DetailView):
    model = Mailing
    template_name = 'client/mailing_detail.html'
    context_object_name = 'mailing'
    success_url = reverse_lazy('client:mailing_list')


class  MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'client/mailing_form.html'
    success_url = reverse_lazy('client:mailing_list')


class  MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'client/mailing_delete.html'
    success_url = reverse_lazy('client:mailing_list')
