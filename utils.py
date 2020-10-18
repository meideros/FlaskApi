ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tif'}
regexEmail = '^[a-z0-9._-]+@[a-z0-9._-]+\.[a-z]{2,6}$'
regexPhoneNumber = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
