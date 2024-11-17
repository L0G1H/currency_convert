from setuptools import setup

setup(
    name="currency_convert",
    version="0.1",
    packages=["currency_convert"],
    install_requires=[
        'requests',
        'bs4',
        'CurrencyConverter'
    ],
)
