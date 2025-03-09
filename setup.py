import os
from setuptools import setup, Extension
from Cython.Build import cythonize

is_windows = os.name == 'nt'

# Windows-specific configurations
libraries = ['rocksdb', 'shlwapi', 'rpcrt4'] if is_windows else ['rocksdb']
compile_args = ['/std:c++17', '/EHsc', '/D_WIN32_WINNT=0x0601'] if is_windows else ['-std=c++17']

ext = Extension(
    'rocksdb._rocksdb',
    sources=['rocksdb/rocksdb.pyx'],
    include_dirs=[
        os.path.join(os.environ.get('CONDA_PREFIX', ''), 'Library/include')
    ],
    library_dirs=[
        os.path.join(os.environ.get('CONDA_PREFIX', ''), 'Library/lib')
    ],
    libraries=libraries,
    language='c++',
    extra_compile_args=compile_args,
    extra_link_args=['/MANIFEST'] if is_windows else []
)

setup(
    name='python-rocksdb',
    version='0.9.0',
    packages=['rocksdb'],
    ext_modules=cythonize(
        [ext],
        compiler_directives={'language_level': "3"},
        force=True
    ),
    # ... other metadata
)
