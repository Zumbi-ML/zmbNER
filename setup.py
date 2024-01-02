from setuptools import setup, find_packages

setup(
    name='zmbner',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'transformers==4.35.2',
        'torch==2.1.2'
    ],
)