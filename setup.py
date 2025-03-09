from setuptools import setup, Extension
from Cython.Build import cythonize
import os

is_windows = os.name == 'nt'

libraries = ['rocksdb', 'shlwapi', 'rpcrt4'] if is_windows else ['rocksdb']
extra_compile_args = ['/std:c++17', '/EHsc', '/D_WIN32_WINNT=0x0601'] if is_windows else ['-std=c++17']

rocksdb_extension = Extension(
    'rocksdb._rocksdb',
    sources=['rocksdb/_rocksdb.pyx'],
    include_dirs=[
        os.getenv('INCLUDE_PATH', ''),
        os.path.join(os.getenv('CONDA_PREFIX', ''), 'Library/include')
    ],
    library_dirs=[
        os.getenv('LIB_PATH', ''),
        os.path.join(os.getenv('CONDA_PREFIX', ''), 'Library/lib')
    ],
    libraries=libraries,
    language='c++',
    extra_compile_args=extra_compile_args,
    # Windows-specific linker flags
    extra_link_args=['/MANIFEST'] if is_windows else []
)

setup(
    ext_modules=cythonize(
        [rocksdb_extension],
        compiler_directives={'language_level': "3"},
        force=True  # Ensure rebuild when environment changes
    ),
    # ... rest of your setup config
)
