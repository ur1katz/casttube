from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='casttube',
      version='0.1.0',
      description='YouTube chromecast api',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/ur1katz/casttube',
      author='Uri Katz',
      author_email='4urikatz@gmail.com',
      license='MIT',
      packages=['casttube'],
      zip_safe=False,
      keywords = ['youtube', 'chromecast', 'youtube-api'],
      install_requires=['requests'])
