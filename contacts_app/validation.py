# Створіть функцію validate_email(email).
# Кожна з функцій повинна повертати кортеж з двох значень:
# - True або False
# - текст повідомлень
from string import digits


def validate_email(email):
    if "@" not in email:
        return False, "Email має містити @."

    if "." not in email:
        return False, "Email має містити крапку."

    return True, ""

def validate_phone(phone):
    if not phone:
        return False,
    if phone[0] =="+":
        digits = phone[1:]
    else:
        digits = phone
    if not digits.isdigit():
        return False, "Телефон має містити лише цифри і знак + на початку"
    if len(digits) !=12:
        return False, "Телефон має містити 12 цифр."

    return True, ""


