# Automatically generated from poetry/pyproject.toml
# flake8: noqa
# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['c7n_kube',
 'c7n_kube.actions',
 'c7n_kube.resources',
 'c7n_kube.resources.apps',
 'c7n_kube.resources.core']

package_data = \
{'': ['*']}

install_requires = \
['argcomplete (>=2.0.0,<3.0.0)',
 'attrs (>=22.1.0,<23.0.0)',
 'boto3 (>=1.24.87,<2.0.0)',
 'botocore (>=1.27.87,<2.0.0)',
 'c7n (>=0.9.19,<0.10.0)',
 'docutils (>=0.17.1,<0.18.0)',
 'importlib-metadata (>=4.13.0,<5.0.0)',
 'importlib-resources (>=5.9.0,<6.0.0)',
 'jmespath (>=1.0.1,<2.0.0)',
 'jsonschema (>=4.16.0,<5.0.0)',
 'kubernetes>=10.0.1,<11.0.0',
 'pkgutil_resolve_name (>=1.3.10,<2.0.0)',
 'pyrsistent (>=0.18.1,<0.19.0)',
 'python-dateutil (>=2.8.2,<3.0.0)',
 'pyyaml (>=6.0,<7.0)',
 's3transfer (>=0.6.0,<0.7.0)',
 'six (>=1.16.0,<2.0.0)',
 'tabulate (>=0.8.10,<0.9.0)',
 'typing-extensions (>=4.3.0,<5.0.0)',
 'urllib3 (>=1.26.12,<2.0.0)',
 'zipp (>=3.8.1,<4.0.0)']

setup_kwargs = {
    'name': 'c7n-kube',
    'version': '0.2.18',
    'description': 'Cloud Custodian - Kubernetes Provider',
    'license': 'Apache-2.0',
    'classifiers': [
        'License :: OSI Approved :: Apache Software License',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Distributed Computing'
    ],
    'long_description': '# Custodian Kubernetes Support\n\n\nWork in Progress - Not Ready For Use.\n\n',
    'long_description_content_type': 'text/markdown',
    'author': 'Cloud Custodian Project',
    'author_email': 'cloud-custodian@googlegroups.com',
    'project_urls': {
       'Homepage': 'https://cloudcustodian.io',
       'Documentation': 'https://cloudcustodian.io/docs/',
       'Source': 'https://github.com/cloud-custodian/cloud-custodian',
       'Issue Tracker': 'https://github.com/cloud-custodian/cloud-custodian/issues',
    },
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
