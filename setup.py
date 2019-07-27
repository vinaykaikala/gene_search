from setuptools import setup, find_packages

setup(
    name='gene_query',
    version='1.0.0',
    description='List the gene details on search',
    url='https://github.com/vinaykaikala/gene_search.git',
    author='Vinay kaikala',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='embl gene',

    packages=find_packages(),

    install_requires=['flask-restplus==0.12.1', 'Flask-SQLAlchemy==2.4.0', 'requests', 'click', "pytest==5.0.1", "PyMysql==0.9.3"],

    entry_points={
        'console_scripts': [
            'genequery_api = gene_query.app:main'
        ]
    }
)
