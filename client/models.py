from django.db import models

class Client(models.Model):
    email = models.EmailField(max_length=150, unique=True, verbose_name='Email', help_text='Введите ваш email')
    first_name = models.CharField(max_length=50, verbose_name='Имя', help_text='Введите ваше имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', help_text='Введите вашу фамилию')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', help_text='Введите ваше отчество')
    comment = models.TextField(verbose_name='Комментарий', help_text='Напишите вам комментарий')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name='Тема письма', help_text='Напишите тему письма')
    body = models.TextField(verbose_name='Тело письма', help_text='Напишите содержимое письма')

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

    def __str__(self):
        return f"Рассылка {self.pk} ({self.is_status})"



