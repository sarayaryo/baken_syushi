from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5c#8=#i4vfz-pt&)d#-u_dew@l97!11=anqc@)1+y2^=!re!r_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Logging settings
LOGGING = {
    'version':1,
    'disable_existing_loggers':False,

    #logger setting
    'loggers':{
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },
        'baken':{
            'handlers':['console'],
            'level':'DEBUG'  
        },
    },
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler', ##output to console
            'formatter':'dev'
        },
    },
    'formatters':{
        'dev':{
            'format':'\t'.join([  ## output log cut by tab
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'