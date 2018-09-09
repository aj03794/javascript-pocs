- To generate files necessary to upload, first need a `setup.py` in the root in the project

```
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="create_subject",
    version="0.0.2",
    author="Adam Johnston",
    author_email="adamjohnston151@yahoo.com",
    description="Package to expose subject with next, filter, and subscribe methods - based on yurikoex's npm subject-with-filter package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aj03794/create-subject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
```

- Add a `License` file to the root of the project (need to copy and paste text of license you use into the file)

- To do a upload to test.pypi.org use `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
- To download this package `python3 -m pip install --index-url https://test.pypi.org/simple/ create_subject`

- url to upload files to for the first time `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`
- After this first time upload, need to update the version in order update the package
