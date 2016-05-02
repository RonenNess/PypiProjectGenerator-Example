from distutils.core import setup
import os

# get curr dir
curr_dir = os.path.abspath(os.path.dirname(__file__))

# get readme
with open(os.path.join(curr_dir, 'README.md')) as readme_file:
    long_desc = readme_file.read()

# setup
setup(
  name = 'pypiprojectgenerator_example',
  packages = ['pypiprojectgenerator_example'],
  package_data = {'pypiprojectgenerator_example' : ["*.py", "README.md"], },
  version = '1.0.0',
  description = 'An example project generated with PypiProjectGenerator.',
  author = 'Ronen Ness',
  author_email = 'ronen.ness@gmail.com',
  url = 'https://github.com/RonenNess/PypiProjectGenerator-Example',
  download_url = 'https://github.com/RonenNess/PypiProjectGenerator-Example/tarball/1.0.0',
  long_description = long_desc,
  keywords = ['generate', 'pypi', 'package', 'create'],
  classifiers = [],
)
