from setuptools import setup

setup(
    name='TracOpenShiftQuickstart', 
    version='1.0',
    description='OpenShift trac quickstart',
    author='Kelvin Mo',

    install_requires=[
        'Trac == 1.0',
        'MySQL-python',
        'psycopg2',
        'Babel',
        'docutils',
        'Pygments',
        'pytz'
    ],
)
