import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="awakenedhaki",
    version="0.1.0",
    author="Rodrigo Vallejos",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/awakenedhaki/crossref-api-python-client",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.6',
)