from setuptools import setup
from wrapper_google import VERSION

setup(name='simple_google_wrapper',
      version=VERSION,
      description='Simple wrapper for google APIs.',
      url='https://github.com/alves-dev/get_archives_driver',
      author='Igor Moreira',
      author_email='alvesmoreiraigor@gmail.com',
      license='MIT',
      packages=['driver', 'wrapper_google'],
      zip_safe=False)
