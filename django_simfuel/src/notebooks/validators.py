def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.ipynb']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please support a jupyter notebook with the ending .ipynb.')