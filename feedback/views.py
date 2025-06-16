from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import FeedbackCreateForm
from .models import Feedback
from .email import send_contact_email_message
from .utils import get_client_ip


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    success_message = "Ваше письмо успешно отправлено администрации сайта"
    template_name = "feedback/feedback.html"
    extra_context = {"title": "Контактная форма"}
    success_url = reverse_lazy("feedback:feedback_massage")


    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            if self.request.user.is_authenticated:
                feedback.user = self.request.user
            send_contact_email_message(
                feedback.subject,
                feedback.email,
                feedback.content,
                feedback.ip_address,
                feedback.user_id,
            )
        return super().form_valid(form)


def feedback_massage(request):
    context = {
        "title": "Успешная отправка",
        }
    return render(request, "feedback/feedback_massage.html", context=context)
