from setuptools import setup, find_packages

setup(
    name="django_es_indexer",
    version="2.1.6",
    description="Elasticsearch indexing from a django app",
    author="Mirus Research",
    author_email="frank@mirusresearch.com",
    packages=find_packages(),
    url='https://github.com/mirusresearch/django_es_indexer',
    license='MIT license, see LICENSE.txt',
    install_requires=[
        'six>=1.11.0',
    ],
)
