"""
Django settings for cpc project.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
PRODUCTION = ENVIRONMENT in ["PROD", "prod", "production", "PRODUCTION"]

DEBUG = not PRODUCTION

ALLOWED_HOSTS = ["*"]
if PRODUCTION:
    APP_HOSTNAME = os.getenv("APP_HOSTNAME")
    CSRF_TRUSTED_ORIGINS = [
        f"https://{hostname.strip()}" for hostname in APP_HOSTNAME.split(",")
    ]
else:
    CSRF_TRUSTED_ORIGINS = ["http://*", "https://*"]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

print("ENVIRONMENT:", ENVIRONMENT)
if ENVIRONMENT == "dev" or ENVIRONMENT == "development" or ENVIRONMENT is None:
    GIT_HASH = "development"
else:
    GIT_HASH = os.getenv("GIT_HASH", "N/A")
