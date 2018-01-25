from setuptools import setup

setup(
    name='magnum-microservices',
    version='0.0.1a1',
    install_requires=["requests==2.13.0"],
    packages=['magnum_microservices'],
    license='Apache License 2.0',
    author='OptimalBI LTD',
    url='http://www.optimalbi.com/',
    author_email='tim.gray@optimalbi.com',
    description='A client library for connecting to Magnum Microservices Server.',
    keywords=['Microservices']
)
