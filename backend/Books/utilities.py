from django.forms import ValidationError




def validate_max_rating(value):
    if value > 5.0: 
        raise ValidationError("The maximum rating allowed is 5.0.")