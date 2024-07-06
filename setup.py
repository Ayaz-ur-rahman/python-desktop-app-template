from setuptools import setup, find_packages

setup(
    name="python_desktop_app_template",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt5",
        "vtk",
    ],
    entry_points={
        "console_scripts": [
            "python_desktop_app_template = main:main",
        ],
    },
)
