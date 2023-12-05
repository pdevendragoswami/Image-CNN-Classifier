import setuptools

__version__ = '0.0.1'

REPO_NAME = 'CNNClassifier'
AUTHOR_NAME = 'Devendra Goswami'
SRC_REPO = "CNNClassifier"
AUTHOR_Email = 'pdevendragoswami@gmail.com'

with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_Email,
    description= 'this is an image classification project',
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_url ={"Bug Tracker":f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}"},
    package_dir = {"":"src"},
    packages=setuptools.find_package(where='src')

)