from setuptools import find_packages, setup
from typing import List

setup(
    name="SMS_SPAM_HAM_CLASSIFIER",
    version="1.0.0",
    author="Anshika Rajput",
    author_email="anshika776rajput@gmail.com",
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "nltk",
        "stop-words",
        "stemmer",
        "lemmatizer",
        "matplotlib",
        "seaborn",
        "scipy"
    ],
    packages=find_packages()
)