from django.core.validators import ValidationError


def letters_numbers_underscores(value):
    for char in value:
        if not char.isalnum() and char != '_':
            raise ValidationError("Username can contain only letters, numbers and underscores!")


def only_letters(value):
    if not value.isalpha():
        raise ValidationError("Name can contain only letters!")


def min_length(value):
    if len(value) < 8:
        raise ValidationError("Password must be at least 8 characters long!")


def must_have_digit_and_letter(value):
    if not any(char.isalpha() for char in value):
        raise ValidationError("Password must have at least one letter!")
    if not any(char.isdigit() for char in value):
        raise ValidationError("Password must have at least one number!")


def image_size(image):
    if image.file.size > 5*1024*1024:
        raise ValidationError("Image size cannot be more than 5MB!")