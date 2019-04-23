from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

# requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="osudata",
    version="0.0.1",
    author="al1",
    author_email="support@al1.space",
    description="for collecting and analyzing osu! game data",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/osu-scripts/osudata/",
    packages=find_packages(),
    # install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3.0",
    ],
)