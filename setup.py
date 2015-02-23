from setuptools import setup, find_packages
from pip.req import parse_requirements


NAME = "probability"

# Dynamically calculate the version based on __version__.
version = __import__(NAME).__version__

requirements_path = "requirements.txt"
test_requirements_path = "test_requirements.txt"


def get_requirements(path):
    return map(lambda ir: str(ir.req), parse_requirements(path))


setup(
    name=NAME,
    packages=find_packages(exclude=['tests*']),
    version=version,
    description='probability',
    author='user',
    license="BSD",
    keywords=["probability"],
    # parse_requirements() returns generator of pip.req.InstallRequirement objects
    install_requires=get_requirements(requirements_path),
    tests_require=get_requirements(test_requirements_path),
)
