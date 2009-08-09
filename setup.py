from setuptools import setup, find_packages

setup( name ="dpaster",
	version  ="0.1",
	packages = find_packages(),
	install_requires = ["twill","argparse"],
	scripts = ["dpaster/dpaster_run.py"]
)
