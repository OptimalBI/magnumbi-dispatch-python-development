from setuptools import setup

setup(
    name='magnum-microservices',
    version='0.0.1a1',
    install_requires=["requests>=2.18", "simplejson==3.8.2"],
    packages=['magnumbi_depot'],
    license='Apache License 2.0',
    author='OptimalBI LTD',
    url='http://www.optimalbi.com/',
    author_email='hey@optimalbi.com',
    description='A client library for connecting to MagnumBI Dispatch Server.',
    keywords=['Microservices', 'MagnumBI', 'Cloud']
)
