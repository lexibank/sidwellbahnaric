from setuptools import setup
import sys
import json


PY2 = sys.version_info.major == 2
with open('metadata.json', **({} if PY2 else {'encoding': 'utf-8'})) as fp:
    metadata = json.load(fp)


setup(
    name='lexibank_sidwellbahnaric',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['lexibank_sidwellbahnaric'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'lexibank.dataset': [
            'sidwellbahnaric=lexibank_sidwellbahnaric:Dataset',
        ]
    },
    extras_require={
        'test': [
            'pytest-cldf',
        ]},
    install_requires=[
        'pylexibank>=3.0',
    ]
)
