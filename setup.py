#!/usr/bin/env python
from distutils.core import setup

import db_email_backend

long_description = open('README').read()

setup_args = dict(
    name='django-db-email-backend',
    version=db_email_backend.__version__,
    description='Django email backend for storing messages to a database.',
    long_description=long_description,
    author='Jeremy Satterfield',
    author_email='jsatt@jsatt.com',
    url='https://github.com/jsatt/django-db-email-backend',
    license="MIT License",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
    ],
    packages=['db_email_backend'],
    install_requires=[
        "django>=1.4",
    ],
)

if __name__ == '__main__':
    setup(**setup_args)