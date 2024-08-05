from setuptools import setup, find_packages

setup(
    name="lru_cache",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={
        "dev": ["pytest", "pytest-cov"],
    },
    author="Emmanuel Mwangi",
    author_email="emmanuelm@gmail.com",
    description="A Least Recently Used (LRU) Cache implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)