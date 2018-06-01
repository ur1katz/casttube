from setuptools import setup

setup(name='casttube',
      version='0.1.0',
      description='YouTube chromecast api',
      url='http://github.com/ur1katz/casttube',
      author='Uri Katz',
      author_email='4urikatz@gmail.com',
      license='MIT',
      packages=['casttube'],
      zip_safe=False,
      keywords = ['youtube', 'chromecast', 'youtube-api'],
      install_requires=['requests'])
