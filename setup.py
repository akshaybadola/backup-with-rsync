from setuptools import setup

from rsync_backup import __version__

description = "Simple backup wrapper with configuration over rsync for regularly backing up via command line."

with open("README.org") as f:
    long_description = f.read()

setup(
    name="backup-with-rsync",
    version=__version__,
    description=description,
    long_description=long_description,
    url="https://github.com/akshaybadola/backup-with-rsync",
    author="Akshay Badola",
    license="MIT",
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
