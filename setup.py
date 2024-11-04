import shlex
from setuptools import setup
from rsync_backup import __version__

description = "Simple backup wrapper with configuration over rsync for regularly backing up via command line."

try:
    from common_pyutil.proc import which, call
    with open("README.org") as f:
        long_description = f.read()
        pandoc = which("pandoc")
        if "no pandoc" in pandoc:
            print("Cannot convert long description as pandoc not found.\n" +
                  "Long description will be set to same as short description")
        else:
            long_description, _ = call(shlex.split("pandoc -f org -t rst"), input=long_description)
except ModuleNotFoundError:
    print("common_pyutil not found. Will not read long description")
    long_description = ""

setup(
    name="backup-with-rsync",
    version=__version__,
    description=description,
    long_description=long_description,
    url="https://github.com/akshaybadola/backup-with-rsync",
    author="Akshay Badola",
    license="MIT",
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: System :: Networking",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Natural Language :: English",
    ],
    packages=["rsync_backup"],
    include_package_data=True,
    keywords='rsync backup',
    python_requires=">=3.7, <=4.0",
    install_requires=["PyYAML"],
    entry_points={
        'console_scripts': [
            'backup-with-rsync = rsync_backup.__main__:main',
        ],
    }
)
