
import importlib
import os
import platform
import sys

from os.path import join
from setuptools import  setup, find_packages
from setuptools.command.build_ext import build_ext



DISTNAME = "Decision_Making"
DESCRIPTION = "A set of python modules for machine learning."
with open("README.md") as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = ""
MAINTAINER_EMAIL = ""
URL = ""
DOWNLOAD_URL = ""
LICENSE = ""
PROJECT_URLS = {
    "Documentation": "",
    "Source Code": "",
}
VERSION = "1.0.0"

from decision_making import min_dependency as md


def setup_package():
    python_requires = ">=3.9"
    # required_python_version = (3, 9)
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
        classifiers=[
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Development Status :: 5 - Production/Stable",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Unix",
            "Operating System :: MacOS",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
        ],
        python_requires=python_requires,
        install_requires=md.install_requires,
        package_data={
            "": ["*.csv", "*.gz", "*.txt", "*.pxd", "*.rst", "*.jpg", "*.css"]
        },
        zip_safe=False,  # the package can run out of an .egg file
    )

    # commands = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    # if not all(
    #     command in ("egg_info", "dist_info", "clean", "check") for command in commands
    # ):
    #     if sys.version_info < required_python_version:
    #         required_version = "%d.%d" % required_python_version
    #         raise RuntimeError(
    #             "Decision_Making requires Python %s or later. The current"
    #             " Python version is %s installed in %s."
    #             % (required_version, platform.python_version(), sys.executable)
    #         )

    #     check_package_status("numpy", min_deps.NUMPY_MIN_VERSION)
    #     check_package_status("scipy", min_deps.SCIPY_MIN_VERSION)

    #     _check_cython_version()
    #     metadata["ext_modules"] = configure_extension_modules()
    #     metadata["libraries"] = libraries
    setup(**metadata)

if __name__ == "__main__":
    setup_package()