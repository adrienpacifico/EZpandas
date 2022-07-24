import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="ez_pandas",
    version="0.0.1",
    author="adrien pacifico",
    author_email="adrienpacifico@gmail.com",
    description="Sugary and more explit syntax for pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adrienpacifico/EZpandas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)