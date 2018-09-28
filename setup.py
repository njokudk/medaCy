from setuptools import setup
from medacy import __version__, __authors__

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='medacy',
    version=__version__,
    license='GNU GENERAL PUBLIC LICENSE',
    description='Medical Natural Language Processing (NLP) with spaCy',
    long_description=readme(),
    packages=['medacy'],
    url='https://github.com/NanoNLP/medaCy',
    author=__authors__,
    author_email='contact@andriymulyar.com', #TODO general nlp lab email?
    keywords='natural-language-processing medical-natural-language-processing machine-learning nlp-library metamap clinical-text-processing',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Topic :: Text Processing :: Linguistic',
        'Intended Audience :: Science/Research'
    ],
    install_requires=[
        'spacy>=2.0.12',
        'scikit-learn>=0.20.0',
        'sklearn-crfsuite'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=False

)