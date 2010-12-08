from setuptools import setup
import os

try:
    long_desc = open(os.path.join(os.path.dirname(__file__),'README')).read()
except (IOError, OSError):
    long_desc = ''

try:
    reqs = open(os.path.join(os.path.dirname(__file__),'requirements.txt')).read()
except (IOError, OSError):
    reqs = ''

setup(
    name = "django-recaptcha-comments",
    version = "0.1",
    author = "Bill Mill",
    author_email = "bill.mill@gmail.com",
    description = "An application to make it easy for django sites to require reCAPTCHA on comments",
    long_description = long_desc,
    license = "BSD",
    url = "http://github.com/llimllib/django-recaptcha-comments",
    packages = [
        "recaptcha_comments",
        "recaptcha_comments.templatetags",
    ],
    install_requires = reqs,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
