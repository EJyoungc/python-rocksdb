# python-rocksdb Windows Build

[![Windows Build Status](https://img.shields.io/badge/Windows-Build-informational)](https://github.com/EJyoungc/python-rocksdb/actions)
![Python Versions](https://img.shields.io/badge/Python-3.8|3.9|3.10|3.11|3.12-blue)

*Created and maintained by EJ*

## Installation

### From PyPI
\```bash
pip install python-rocksdb
\```

### From Source
\```bash
git clone https://github.com/yourusername/python-rocksdb.git
cd python-rocksdb
conda env create -f conda-environment.yml
conda activate rocksdb-build
python setup.py install
\```

## Basic Usage
\```python
import rocksdb

# Create database
db = rocksdb.DB("test.db", rocksdb.Options(create_if_missing=True))

# Insert data
db.put(b"key1", b"value1")

# Retrieve data
print(db.get(b"key1"))  # Output: b'value1'
\```

## Project Structure
\```
.
├── .github/
│   └── workflows/
│       └── build_windows_wheels.yml
├── rocksdb/
│   ├── __init__.py
│   ├── _rocksdb.pyx
│   └── rocksdb.pxd
├── tests/
│   ├── __init__.py
│   └── test_basic.py
├── LICENSE
├── MANIFEST.in
├── README.md
├── setup.cfg
└── setup.py
\```

## Development
\```bash
# Run tests
pytest tests/

# Build wheel
python setup.py bdist_wheel
\```

## Credits
*This entire project was created by EJ with special attention to Windows compatibility and build automation.*

---

**NOTE**: Replace "yourusername" with your actual GitHub username when using this template.
