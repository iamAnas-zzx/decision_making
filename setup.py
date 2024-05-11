
from os.path import join
from setuptools import  setup, find_packages




DISTNAME = "decision_making"
DESCRIPTION = "A python package for Fuzzy-Multi Criteria Decision Making problems."
with open("README.md") as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = "Ahmad Anas, Eeshan Anand"
MAINTAINER_EMAIL = "anasahamd9616@gmail.com"
URL = "https://github.com/iamAnas-zzx/decision_making.git"
DOWNLOAD_URL = ""
LICENSE = "MIT"
PROJECT_URLS = {
    "Documentation": "http://github.com/iamAnas-zzx/decision_making.git",
    "Source Code": "https://github.com/iamAnas-zzx/decision_making.git",
}
VERSION = "1.0.0"

from decision_making import min_dependency as md


def setup_package():
    python_requires = ">=3.9"
    metadata = dict(
        packages=find_packages(),
        name=DISTNAME,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        download_url=DOWNLOAD_URL,
        project_urls=PROJECT_URLS,
        version=VERSION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        classifiers=[
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Development Status :: 5 - Production/Stable",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy"
        ],
        python_requires=python_requires,
        install_requires=md.install_requires,
        package_data={
            "": ["*.csv", "*.gz", "*.txt", "*.pxd", "*.rst", "*.jpg", "*.css"]
        },
        zip_safe=False,  # the package can run out of an .egg file
    )
    setup(**metadata)

if __name__ == "__main__":
    setup_package()