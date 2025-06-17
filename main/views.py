from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import context

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.conf import settings

from axes.decorators import axes_dispatch
from django.views.decorators.http import require_http_methods
from axes.helpers import get_client_username
from axes.signals import user_locked_out
from axes.models import AccessAttempt  # Для ручного управления

from main.utils import q_search
from route.models import Route
from country.models import Сountry
from brewery.models import Brewery
from feedback.models import Feedback
from feedback.forms import FeedbackCreateForm
from feedback.email import send_contact_email_message
from feedback.utils import get_client_ip
from django.views.generic import TemplateView


@axes_dispatch  # Добавляем декоратор axes
@require_http_methods(["GET", "POST"])  # Разрешаем оба метода
def admin_prelogin(request):
    if request.method == "POST":
        if request.POST.get("pre_password") == settings.ADMIN_PRE_PASSWORD:
            # Сбрасываем счетчик попыток для IP
            AccessAttempt.objects.filter(
                ip_address=request.META.get("REMOTE_ADDR")
            ).delete()
            return redirect("admin:index")
        # Логируем неудачную попытку
        user_locked_out.send(
            sender=None,
            request=request,
            username=get_client_username(request),
            failure_limit=settings.AXES_FAILURE_LIMIT,
        )
        messages.warning(request, "Неверный пароль для доступа к админ-панели")
        return render(request, "main/admin_prelogin.html")  # Возвращаем форму с ошибкой
    # GET-запрос - просто отображаем форму
    return render(request, "main/admin_prelogin.html")

@user_passes_test(lambda u: u.is_superuser)
def protected_admin_redirect(request):
    return redirect("admin:index")


def index(request):

    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)

    if query:
        routes = q_search(query)
    else:
        routes = Route.objects.all()

    breweries = Brewery.objects.all()
    countries = Сountry.objects.all()

    route_dark = range(1, 6)
    route_light = range(6, 70)
    route_disabled = range(70, 100)
    route_20 = range(1, 21)

    paginator = Paginator(routes, 20)
    current_page = paginator.page(int(page))

    paginator = Paginator(breweries, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "title": "Главная",
        "routes": current_page,
        "route_dark": route_dark,
        "route_light": route_light,
        "route_disabled": route_disabled,
        "route_20": route_20,
        "breweries": breweries,
        "page_obj": page_obj,
        "countries": countries,
        # "country": country,
    }
    return render(request, "main/index.html", context=context)


def about(request):
    context = {
        "title": "Информация",
    }
    return render(request, "main/about.html", context=context)


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    success_message = "Ваше письмо успешно отправлено администрации сайта"
    template_name = "main/write.html"
    extra_context = {"title": "Контактная форма"}
    success_url = reverse_lazy("main:feedback_massage")

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
    return render(request, "main/write_massage.html", context=context)


def oferta_view(request):
    context = {
        "title": "Договор-оферта",
    }
    return render(request, "main/oferta.html", context)


def privacy_view(request):
    context = {
        "title": "Политика конфиденциальности",
    }
    return render(request, "main/privacy.html", context)
