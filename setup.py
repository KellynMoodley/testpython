import setuptools
import os
import sys

try:
    import multiprocessing  # noqa
except ImportError:
    pass

setuptools.setup(
    name='herokupython',  # Replace with your project name
    version='0.1',  # Define your project version
    setup_requires=['pbr>=1.8'],  # Specify PBR version requirement
    pbr=True,
    install_requires=[
        'requests',  # Add necessary dependencies here
        'pyaudio',  # Add necessary dependencies here
    ]
)
