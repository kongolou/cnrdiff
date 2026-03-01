from setuptools import setup, find_packages

setup(
    name="cnrdiff",
    version="1.2.0",
    description="A library used to compare signal-to-noise ratio",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="Sheng Guoliang",
    author_email="shengguoliang@sinognss.com",
    python_requires=">=3.10",
    packages=find_packages(where=".", include=["cnrdiff*"]),
    install_requires=[
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
    ],
    keywords=["cnr", "signal-to-noise", "gnss", "rinex", "bnc"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering",
    ],
    url="https://github.com/sinognss/cnrdiff",
    project_urls={
        "Homepage": "https://github.com/sinognss/cnrdiff",
        "Repository": "https://github.com/sinognss/cnrdiff",
        "Issues": "https://github.com/sinognss/cnrdiff/issues",
    },
)
