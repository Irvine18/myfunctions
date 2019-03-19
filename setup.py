from setuptools import setup, find_packages

setup(
    name='myfunctions',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='my python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Irvine18/myfunction',
    author='<Irvine>',
    author_email='<ikchipindu18@gmail.com>'
)
