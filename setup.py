import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ca-taxes",
    version="1.0.1",
    description="Django App for handling California Taxes",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/stasdavydov/ca-taxes",
    author="Stas Davydov",
    author_email="davidovsv@yandex.ru",
    license="Unlicense License",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["ca_taxes"],
    include_package_data=True,
    install_requires=["requests", "Django"],
)
