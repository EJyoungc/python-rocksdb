#!/usr/bin/env python3
import os
import sys
from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

# Define common settings
if os.name == "nt":
    # Windows-specific settings
    # Prefer conda environment paths if available
    if "CONDA_PREFIX" in os.environ:
        conda_prefix = os.environ["CONDA_PREFIX"]
        include_dirs = [os.path.join(conda_prefix, "Library", "include")]
        library_dirs = [os.path.join(conda_prefix, "Library", "lib")]
    else:
        # Fallback: adjust these paths to your local RocksDB installation on Windows
        include_dirs = [r"C:\RocksDB\include"]
        library_dirs = [r"C:\RocksDB\lib"]

    # MSVC uses /std:c++14 (if supported)
    extra_compile_args = ["/std:c++14"]
    libraries = ["rocksdb"]  # Add other required libraries (e.g. snappy, lz4) if needed
else:
    # Non-Windows (Linux, macOS) settings
    include_dirs = []
    library_dirs = []
    if "CONDA_PREFIX" in os.environ:
        conda_prefix = os.environ["CONDA_PREFIX"]
        include_dirs.append(os.path.join(conda_prefix, "include"))
        library_dirs.append(os.path.join(conda_prefix, "lib"))
    # Also check common system locations
    include_dirs.extend(["/usr/local/include", "/usr/include"])
    library_dirs.extend(["/usr/local/lib", "/usr/lib"])
    extra_compile_args = ['-std=c++11']
    libraries = ['rocksdb']

# Define the extension module
ext = Extension(
    "rocksdb._rocksdb",
    sources=["rocksdb/_rocksdb.pyx", "rocksdb/rocksdb.cpp"],
    include_dirs=include_dirs,
    library_dirs=library_dirs,
    libraries=libraries,
    extra_compile_args=extra_compile_args,
)

# Only use cythonize if the .pyx file exists.
if os.path.exists("rocksdb/rocksdb.pyx"):
    ext_modules = cythonize([ext], compiler_directives={'language_level': "3"})
else:
    ext_modules = [ext]


# Optionally load long description from README.md
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="python-rocksdb",
    version="0.7.0",
    description="Python bindings for RocksDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="EJ Young",
    url="https://github.com/EJyoungc/python-rocksdb",
    packages=find_packages(),
    ext_modules=ext_modules,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
    zip_safe=False,
)
