from django.core.validators import ValidationError


def image_size(image):
    if image.file.size > 5*1024*1024:
        raise ValidationError("Image size cannot be more than 5MB!")

