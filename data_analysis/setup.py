from setuptools import setup, find_packages

setup(
        name='baseball-qualifying-offer',
        version='1.0',
        author='Qianyun Zhu',
        authour_email='zhuchanyoon@gmail.com',
        packages=find_packages(exclude=('tests', 'docs')),
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
)