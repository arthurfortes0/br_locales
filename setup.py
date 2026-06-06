"""Setup configuration for br_locales package."""

from setuptools import setup, find_packages

with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='br_locales',
    version='0.0.91',
    license='MIT License',
    author='Arthur Fortes',
    author_email='fortes.arthur@gmail.com',
    description='Brazilian cities and states data from IBGE (Brazilian Institute of Geography and Statistics)',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    keywords=['cities', 'states', 'brazil', 'ibge', 'locations', 'geographic'],
    packages=find_packages(),
    package_data={'br_locales': ['states_and_cities_10_22.json']},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
