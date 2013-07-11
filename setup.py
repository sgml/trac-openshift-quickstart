from setuptools import setup

setup(
    name='TracOpenShiftQuickstart', 
    version='1.0',
    description='OpenShift trac quickstart',
    author='Kelvin Mo',

    install_requires=[
        # The web server
        'greenlet',
        'gevent',

        # Trac and various dependencies
        'Trac == 1.0',
        'MySQL-python',
        'psycopg2',
        'Babel',
        'docutils',
        'Pygments',
        'pytz',

        # Some useful plugins
        'TracAccountManager',

        # Add your trac plugins here

    ],
)
