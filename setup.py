from setuptools import setup


def readme() -> None:
    """Long description."""
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="ppi",
    version="1.2.2b1",
    description="Simple utility to create new Python -projects with.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="automation utility",
    url="https://github.com/nikkelarsson/ppi",
    author="Niklas Larsson",

    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],

    packages=["ppi"],
    data_files=[("man/man1", ["docs/ppi.1"])],
    python_requires=">=3.8",  # This parameter requires setuptools >=24.2.0
    install_requires=["colorama"],
    entry_points={"console_scripts": ["ppi=ppi.main:main"]},
    include_package_data=True,
    zip_safe=False,
)
