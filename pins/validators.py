







from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 20971520:
        raise ValidationError("You cannot upload a file with a size of more than 20MB")
    else:
        return value