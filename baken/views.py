from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import InquiryForm
import logging

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('baken:inquiry') ###reverse.lazyで相対的に書く

    def form_valid(self, form):
        form.send_email() ## send to form.py
        messages.sucess(self.request,'メッセージを送信しました！')  ###ERROR, WARNING, INFOもあるよ
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))  ###logger.<ログレベル>(<出力内容>)
        return super().form_valid(form)
