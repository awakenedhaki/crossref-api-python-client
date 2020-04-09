import setuptools

from crossrefapiclient import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crossref-api-client",
    version=__version__,
    author="awakenedhaki",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/awakenedhaki/crossref-api-python-client",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.6',
)