from setuptools import setup, find_packages


base_packages = [
    "rasa>=2.2.0",
    "bpemb>=0.3.2",
    "gensim~=3.8.3",
    "rich>=9.2.0",
    "pandas>=1.0.5",
    "tensorflow>=2.3.0,<2.5",
    "pyphen>=0.11.0",
]

dev_packages = [
    "flake8>=3.6.0",
    "black>=19.10b0",
    "pre-commit>=2.5.1",
    "pytype>=2020.0.0",
    "pytest>=4.0.2",
    "pytest-xdist==1.32.0",
    "mkdocs==1.1",
    "mkdocs-material==5.4.0",
    "mkdocstrings==0.8.0",
    "pymdown-extensions>=7.1",
]

stanza_deps = [
    "stanza>=1.1.1",
]

thai_deps = [
    "pythainlp>=2.2.3",
]

fasttext_deps = [
    "fasttext~=0.9.2",
]

flashtext_deps = [
    "flashtext==2.7",
]

dateparser_deps = [
    "dateparser>=1.0.0",
]

setup(
    name="rasa_nlu_examples",
    version="0.4.2",
    packages=find_packages(exclude=["notebooks", "data"]),
    install_requires=base_packages,
    extras_require={
        "dev": dev_packages,
        "dev-windows": dev_packages + thai_deps,
        "all": dev_packages
        + thai_deps
        + fasttext_deps
        + flashtext_deps
        + stanza_deps
        + dateparser_deps,
        "thai": base_packages + thai_deps,
        "stanza": base_packages + stanza_deps,
        "fasttext": base_packages + fasttext_deps,
        "flashtext": base_packages + flashtext_deps,
        "dateparser": base_packages + dateparser_deps,
    },
)
