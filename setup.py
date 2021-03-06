from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="json_wrapper",
    description="Easy to use JSON wrapper packed with features.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/RGBCube/json_wrapper",
    version="1.2.0",
    author="RGBCube",
    py_modules=["json_wrapper"],
    license="CC0 1.0 Universal"
)
