from setuptools import setup, find_packages

setup(
    name="coding_funtions",
    packages=find_packages(
        include=["coding_functions"]
    ),
    include_package_data=True,
    python_requires=">=3.10",
)
