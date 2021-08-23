def plugin_settings(settings):
    settings.SMOWLCAMERA_BASE_URL = settings.ENV_TOKENS.get('SMOWLCAMERA_URL', '')
    settings.SMOWL_KEY = settings.ENV_TOKENS.get('SMOWL_KEY', '')
    settings.SMOWLCAMERA_FULL_URL = '{}?modality_ModalityName=edxActivity&lang=en&swlLicenseKey={}&type=4&user_idUser'.format(settings.SMOWLCAMERA_BASE_URL, settings.SMOWL_KEY)
    settings.SMOWLCAMERA_INSERTEDXPOST_URL = settings.ENV_TOKENS.get('SMOWLCAMERA_INSERTEDXPOST_URL', '')
    settings.SMOWL_ENTITY = settings.ENV_TOKENS.get('SMOWL_ENTITY', '')