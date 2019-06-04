from setuptools import setup

setup(
    name='ovh-tools',
    version='0.1',
    py_modules=['ovh-tools'],
    install_requires=[
        'Click',
        'ovh',
        'tabulate',
    ],
    entry_points='''
        [console_scripts]
        ovh=main:cli
    ''',
)
