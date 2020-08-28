from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _, ngettext_lazy
from django.core.validators import *


def validate_only_letters(value):
    valor = value.replace(" ", "")
    if not valor.isalpha():
        raise ValidationError(
            _('Los campos Nombre y Apellido no deben contener valores numericos'),
            params={'value': value},
        )


def validate_only_numbers(value):
    valor = value.replace(" ", "")
    if not valor.isdigit():
        raise ValidationError(
            _('Este campo solo admite valores numericos'),
            params={'value': value},
        )

