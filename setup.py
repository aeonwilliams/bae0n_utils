import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bae0n-utils",
    version="0.0.28\9",
    author="Aeon Williams",
    author_email="aeonwilliams@gmail.com",
    description="Utility functions to be used in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aeonwilliams/bae0n_utils/blob/main/README.md",
    packages=setuptools.find_packages(),
    install_requires=[
        'Pillow', 'numpy', 'pandas', 'pathlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)