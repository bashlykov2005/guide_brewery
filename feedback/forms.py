from django import forms
from captcha.fields import CaptchaField
# from django.conf import settings
# from django_recaptcha.fields import ReCaptchaField
# from django_recaptcha.widgets import ReCaptchaV2Checkbox
from .models import Feedback


class FeedbackCreateForm(forms.ModelForm):
    """Форма отправки обратной связи"""
    # Поле капчи
    captcha = CaptchaField(
        label="Введите текст с картинки (можно строчными буквами), для обновления текста перезагрузите страницу",
        error_messages={
            "invalid": "Введен неправильный текст с картинки",
            "required": "Пожалуйста, введите текст с картинки",
        },
    )
    # recaptcha = ReCaptchaField(
    #     widget=ReCaptchaV2Checkbox,
    #     public_key=settings.RECAPTCHA_PUBLIC_KEY,
    #     private_key=settings.RECAPTCHA_PRIVATE_KEY,
    #     label="ReCAPTCHA",
    # )

    agree_to_terms = forms.BooleanField(
        required=True,
        label="Я согласен с политикой конфиденциальности и договором-офертой",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        error_messages={"required": "Необходимо принять условия соглашения"},
    )

    class Meta:
        model = Feedback
        fields = ("subject", "email", "content", "captcha", "agree_to_terms")
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Текст сообщения",
                    "rows": 3,
                    "class": "form-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)

        # Стили для всех полей
        for field in self.fields:
            if field != "agree_to_terms":
                self.fields[field].widget.attrs.update(
                    {"class": "form-control", "autocomplete": "off"}
                )

        # Кастомные placeholder
        self.fields["subject"].widget.attrs["placeholder"] = "Тема сообщения"
        self.fields["email"].widget.attrs["placeholder"] = "Ваш email"
