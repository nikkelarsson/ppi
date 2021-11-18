from setuptools import setup

setup(
    name="ppi",
    version="1.0",
    description="Simple utility to create new Python -projects with.",
    keywords="utility",
    author="Niklas Larsson",
    packages=["ppi"],
    # install_requires=[],
    entry_points={"console_scripts": ["ppi=ppi.main:main"]},
    include_package_data=True,
    zip_safe=False,
)
