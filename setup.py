from setuptools import setup

setup(
    name='site',
    packages=['src/site'],
    include_package_data=True,
    install_requires=[
		'flask',
		'python-dotenv'
	],
)