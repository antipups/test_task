from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_correct_id(person_type: int, value: str):
    """
        Проверка на верное окончание введённого кода, не верно - валидационная ошибка
    :param person_type: тип персоны, 1 - клиент, 2 - юр лицо, 3 - департамент
    :param value: введённое значение
    :return:
    """
    if not str(value).endswith(f'0{person_type}'):
        raise ValidationError(_(f'%(value)s is not a correct number (correct - end with 0{person_type} number)'),
                              params={'value': value},)


def validate_correct_client_id(value: str | int):
    validate_correct_id(person_type=1,
                        value=value)


def validate_correct_legal_person_id(value: str | int):
    validate_correct_id(person_type=2,
                        value=value)


def validate_correct_department(value: str | int):
    validate_correct_id(person_type=3,
                        value=value)
