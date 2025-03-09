# Python-RocksDB Wheel Builder 🐍🔨

*Created by EJ 🎉*

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Ready-blue?logo=githubactions)

## 📄 Table of Contents
- [💡 Overview](#-overview)
- [🚀 Features](#-features)
- [🛠️ Installation](#️-installation)
- [🖥️ Usage](#️-usage)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## 💡 Overview
Automate building Python C++ extensions for **python-rocksdb** using GitHub Actions! This project simplifies creating cross-platform wheel files (`*.whl`) without local setup hassles. Perfect for Windows developers looking for CI/CD-powered builds.

## 🚀 Features
- ✔️ **Cross-Platform**: Build Windows wheels via GitHub Actions
- ✔️ **CI/CD Integration**: Automated workflows on push/pull requests
- ✔️ **Wheel Build**: Ready-to-install `.whl` files
- ✔️ **Simple Setup**: Just push code → GitHub handles the rest
- ✔️ **Customizable**: Easily adapt the workflow for your needs

## 🛠️ Installation

### Requirements
- GitHub Account
- Python 3.10+ (tested with 3.10)
- Visual Studio Build Tools (for C++ extensions)

# Python-RocksDB Wheel Builder 🐍🔨

*Created by EJ 🎉*

## 🛠️ Installation

### Requirements
- GitHub Account
- Python 3.10+
- Visual Studio Build Tools (for C++ extensions)

### Setting Up GitHub Actions

1. **Fork/Clone the Repository**  
   ```bash
   git clone [https://github.com/EJyoungc/python-rocksdb-wheel-builder.git](https://github.com/EJyoungc/python-rocksdb.git)
   ```

2. **Add `requirements.txt`**  
   Create `requirements.txt` with:  
   ```txt
   cython
   rocksdb
   setuptools
   wheel
   ```

3. **Create GitHub Actions Workflow**  
   Add `.github/workflows/build.yml` with:  
   ```yaml
   name: Build Python-RocksDB Wheel
   on: [push, pull_request]
   jobs:
     build:
       runs-on: windows-2019
       steps:
         - name: Checkout Repository
           uses: actions/checkout@v4
         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: '3.10'
         - name: Install Visual Studio Build Tools
           run: |
             choco install visualstudio2019buildtools --package-parameters "--add Microsoft.VisualStudio.Workload.VCTools --includeRecommended --includeOptional"
           shell: powershell
         - name: Install Dependencies
           run: |
             python -m pip install --upgrade pip setuptools wheel
             python -m pip install -r requirements.txt
         - name: Build the Wheel
           run: python setup.py bdist_wheel
         - name: Upload the Wheel Artifact
           uses: actions/upload-artifact@v4
           with:
             name: windows-wheel
             path: dist/*.whl
   ```

4. **Commit and Push Changes**  
   ```bash
   git add .
   git commit -m "Add workflow and dependencies"
   git push origin main
   ```

---

## 🖥️ Usage

1. **Trigger the Build**  
   Push code to GitHub. The workflow runs automatically.

2. **Download the Wheel**  
   After the build completes, download the `.whl` file from the **Actions** tab > Artifacts.

3. **Install the Wheel**  
   ```bash
   pip install path/to/wheel.whl
   ```

---

## 🤝 Contributing

1. **Fork the repository**.  
2. **Create a branch**:  
   ```bash
   git checkout -b my-feature
   ```  
3. **Commit changes**:  
   ```bash
   git commit -am 'Add new feature'
   ```  
4. **Push and create a PR**:  
   ```bash
   git push origin my-feature
   ```

---

## 📜 License  
MIT License. See [LICENSE](LICENSE).
