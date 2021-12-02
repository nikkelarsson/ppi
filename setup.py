from setuptools import setup

setup(
    name="ppi",
    version="1.2.0",
    description="Simple utility to create new Python -projects with.",

    classifiers=[
        "Environment :: Console"
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Build Tools",
    ],

    keywords="utility",
    url="https://github.com/nikkelarsson/ppi",
    author="Niklas Larsson",
    packages=["ppi"],
    install_requires=["colorama"],
    entry_points={"console_scripts": ["ppi=ppi.main:main"]},
    include_package_data=True,
    zip_safe=False,
)
