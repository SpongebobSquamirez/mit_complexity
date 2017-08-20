from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='mit_complexity',
      version='0.7',
      description='An almost-completed data project involving complexity',
      url='http://github.com/weirdalsuperfan/mit_complexity',
      author='Robert Ramirez',
      packages=['mit_complexity'],
      install_requires=[
          'PyMySQL',
          'nltk',
          'beautifulsoup4',
          'scikit-learn'
      ],
      zip_safe=False)