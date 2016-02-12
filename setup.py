from setuptools import setup

setup(
    name='Crypto Pad Rom',
    version='1.0',
    description='Crypto D100 Rom',
    author='Joe Doe',
    author_email='joe.doe@engineer.com',
    url='https://cryptic-sands-9440.herokuapp.com/',
    install_requires=[
            'flask',
            'flask-login',
            'sqlalchemy',
            'flask-sqlalchemy',
            'gunicorn'
    ]
)
