# 🎉 **Project Title: Python-RocksDB Wheel Builder**

## 📄 **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Setting Up GitHub Actions](#setting-up-github-actions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## 💡 **Overview**
The **Python-RocksDB Wheel Builder** project automates the process of building a Python C++ extension for `python-rocksdb` using GitHub Actions. This provides an easy way to create cross-platform wheel files for `python-rocksdb`, without worrying about local setup or dependencies.

---

## 🚀 **Features**
- ✔️ **Cross-Platform**: Supports building on Windows using GitHub Actions
- ✔️ **CI/CD Integration**: Automates the process using GitHub Actions for smooth builds
- ✔️ **Wheel Build**: Builds `.whl` file ready for installation
- ✔️ **Simple Setup**: Just push your code to GitHub, and the process runs automatically
- ✔️ **Easily Customizable**: Modify the workflow to suit your project's specific needs

---

## 🛠️ **Installation**

### **Requirements**
1. **GitHub Account**: You need a GitHub account to store and manage your code.
2. **Python**: Python 3.10 (or any compatible version).
3. **Visual Studio Build Tools**: The necessary tools to build Python C++ extensions on Windows.

### **Setting Up GitHub Actions**
1. **Fork or Clone this Repository**: Clone the repository to your local machine or fork it to your GitHub account.
2. **Add `requirements.txt`**: This file contains the necessary dependencies for the project. Here’s the content:
   
   ```txt
   cython
   rocksdb
   setuptools
   wheel
