import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="YaleKorean",
    version="1.0.0",
    author="SeHaan",
    author_email="alsgk1123@gmail.com",
    description="Korean Yale Romanizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SeHaan/YaleKorean",
    packages=setuptools.find_packages(),
    keywords=['Yale', 'Korean', 'Romanizer', 'linguistics', 'pypi'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)