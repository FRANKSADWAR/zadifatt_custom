from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in zadifatt_custom/__init__.py
from zadifatt_custom import __version__ as version

setup(
	name="zadifatt_custom",
	version=version,
	description="Custom reports for loan management system",
	author="Billy Adwar && OdukTech Limited",
	author_email="billyfranks98@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
