

def get_field_encryption_key():

    from test_django_encrypted_json_fields.models import Key

    #cryptography.fernet.Fernet.generate_key()

    #return '5wGTKAR-R8ieXRHbHqWoTwp29YLvmcFQII2tQdmXAo4='
    return [k.value for k in Key.objects.all()]

