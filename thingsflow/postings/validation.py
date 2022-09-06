import re

from django.core.exceptions import ValidationError


def validate_password(value):
    REGEX_PASSWORD = '^(?=.*\d)[\d]{6,}$'

    if not re.match(REGEX_PASSWORD, value):
        raise ValidationError('INVALID_PASSWORD')