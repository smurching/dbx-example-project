from setuptools import find_packages, setup
from cicd_sample_project import __version__

setup(
    name="cicd_sample_project",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
