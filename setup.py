from setuptools import setup

setup(name='turkishsuffix',
      version='0.1.9',
      description='A package for adding complex suffixes to Turkish words. While doing that,'
                  ' code uses rule set and python\'s string manipulation to enhance quality.'
                  ' You can find examples on GitHub page.',
      keywords='turkish suffix türkçe ek',
      url='http://github.com/yokunjon/turkishsuffix',
      author='yokunjon',
      author_email='yokunjon@gmail.com',
      license='MIT',
      packages=['turkishsuffix'],
      include_package_data=True,
      zip_safe=False)
