# PypiProjectGenerator-Example
An example project generated with PypiProjectGenerator.

Source at [GitHub](https://github.com/RonenNess/PypiProjectGenerator-Example).

Docs at [PythonHosted.org](http://pythonhosted.org/pypiprojectgenerator_example/).

## Install

Install PypiProjectGenerator-Example via pip:

```python
pip install pypiprojectgenerator_example
```

## How to use

TBD

## Build & upload

To build and upload to pypi (more info here http://peterdowns.com/posts/first-time-with-pypi.html):

```
# first to test repo:
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest

# now actually upload to pypi:
python setup.py register -r pypi
python setup.py sdist upload -r pypi
```

To create docs (will be generated into 'site' folder):

```
mkdocs build --clean
```

## Run Tests

From PypiProjectGenerator-Example root dir:

```shell
cd tests
python run_tests.py
```

Note: tests are not included in the pypi package ("pip insall" won't fetch them). 
To run tests please clone from git.

## Changes

## Contact

For bugs use the issue report, for other stuff feel free to contact me at ronen.ness@gmail.com.


__Project structure generated via [PypiProjectGenerator](https://github.com/RonenNess/PypiProjectGenerator).__

