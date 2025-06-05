from django.forms import ModelForm

from client.models import Client, Message, Mailing


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'