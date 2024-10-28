#!/usr/bin/python3

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pelican-read-more",
    version="1.0.0",
    author="Marcin Juszkiewicz",
    author_email="marcin-python@juszkiewicz.com.pl",
    description="Pelican plugin for 'Read more' functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hrw/pelican-read-more",
    project_urls={
        "Bug Tracker": "https://github.com/hrw/pelican-read-more/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    packages=["pelican/plugins/read_more/"],
    python_requires=">=3.6",
    license_files=["LICENSE"],
)
