import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bubbypdf",
    version="0.0.3",
    author="FrenchCommando",
    author_email="martialren@gmail.com",
    description="A script that merges pdf files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FrenchCommando/bubbypdf",
    packages=setuptools.find_packages(),
    install_requires=['pdfrw==0.4'],
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['bubby-pdf=bubbypdf.bubbypdf:main'],
    }
)
