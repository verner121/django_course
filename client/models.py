from django.conf import settings
from django.db import models


class Client(models.Model):
    email = models.EmailField(max_length=150, unique=True, verbose_name='Email', help_text='Введите ваш email')
    full_name = models.CharField(max_length=100, verbose_name='Ф.И.О.',
                                 help_text='Введите ваше Имя, Фамилию и Отчество')
    comment = models.TextField(blank=True, verbose_name='Комментарий', help_text='Напишите вам комментарий')

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="clients",
    )

    def __str__(self):
        return f'{self.full_name} - {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name='Тема письма', help_text='Напишите тему письма')
    body = models.TextField(verbose_name='Тело письма', help_text='Напишите содержимое письма')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="messages",
        default=1,
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
    STATUS_CHOICES = [
        ('Создана', 'Создана'),
        ('Запущена', 'Запущена'),
        ('Завершена', 'Завершена'),
    ]
    datetime_of_first_send = models.DateTimeField()
    datetime_end_of_send = models.DateTimeField()
    is_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Создана')
    messages = models.ForeignKey(Message, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mailings",
    )

    def __str__(self):
        return f"Рассылка {self.pk} ({self.is_status})"


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ('Успешно', 'Успешно'),
        ('Не успешно', 'Не успешно'),
    ]
    datetime_attempt = models.DateTimeField()
    is_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Успешно')
    mail_server_response = models.TextField()
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Попытка {self.mailing_id} - {self.is_status}"
