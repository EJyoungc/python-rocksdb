
from setuptools import setup, Extension
import os

# Get the conda prefix (if you are using a conda environment)
conda_prefix = os.environ.get("CONDA_PREFIX", "")

# Set default paths for the RocksDB headers and library.
# These will usually be inside your conda environment.
rocksdb_include = os.environ.get("ROCKSDB_INCLUDE_DIR", os.path.join(conda_prefix, "include"))
rocksdb_lib_dir = os.environ.get("ROCKSDB_LIB_DIR", os.path.join(conda_prefix, "lib"))

# Define the extension module.
rocksdb_extension = Extension(
    "rocksdb",                             # Name of the Python module
    sources=["src/rocksdb_python.cpp"],    # C++ source file(s)
    include_dirs=[rocksdb_include],         # Directory for header files
    library_dirs=[rocksdb_lib_dir],         # Directory for library files
    libraries=["rocksdb"],                  # Link against the RocksDB library
    language="c++",
    extra_compile_args=["-std=c++17"]       # Use C++17 standard
)

setup(
    name="python-rocksdb",
    version="0.1.0",
    description="Python bindings for RocksDB using C++ for windows",
    author="EJ",
    author_email="techlink@gmxus",
    ext_modules=[rocksdb_extension],
    packages=["python-rocksdb"],  # Your pure Python package folder
)
