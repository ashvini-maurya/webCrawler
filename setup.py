try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Web Crawler for shopping.com',
    'author': 'Ashvini Kumar',
    'author_email': 'ashvinikumar45@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'name': 'web_crawler'
}

setup(**config)
