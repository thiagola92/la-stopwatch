from pathlib import Path

from setuptools import find_packages, setup

long_description = Path("README.md").read_text()

setup(
    name="la-stopwatch",
    version="0.0.8",
    description="Measure the amount of time that elapses between lap times",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagola92/la-stopwatch",
    author="thiagola92",
    author_email="thiagola92@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="stopwatch, timer, timing, clock",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.10",
)
