from setuptools import setup

setup(name='YourAppName', version='1.0',
    description='OpenShift Python-2.7 Community Cartridge based application',
    author='Your Name', author_email='ramr@example.org',
    url='http://www.python.org/sigs/distutils-sig/',

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
