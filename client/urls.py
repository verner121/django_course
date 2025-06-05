from django.urls import path
from client.views import ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    MessageCreateView, MessageDeleteView, MessageDetailView, MessageUpdateView, MessageListView, MailingDeleteView, MailingUpdateView, MailingCreateView, MailingDetailView, MailingListView

from client.apps import ClientConfig

app_name = ClientConfig.name
urlpatterns = [
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/detail/', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/detail/', MessageDetailView.as_view(), name='message_detail'),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/detail/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),

]
