from setuptools import setup

setup(
    name='pushover_notifier',
    version='1.0.0',
    description='A Python library for sending notifications via Pushover',
    py_modules=['pushover_notifier'],
    install_requires=['http.client', 'requests', 'python-dotenv'],
)

