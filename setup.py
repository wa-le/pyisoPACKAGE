from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='pyisocode',
    version='0.0.1',
    description='converts iso code to country name',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/wa-le/pyisocode',
    author='Adewale Adeagbo',
    author_email='waleadeagbo30@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='country',
    packages=find_packages(),
    install_requires=['']
)