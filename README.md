# Network Automation with PyATS

This project demonstrates how to automate network tasks using [PyATS](https://developer.cisco.com/pyats/). Specifically, it connects to Cisco DevNet devices, retrieves running configurations and interface details, and updates interface configurations.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)

---

## Prerequisites

Before using this project, ensure you meet the following requirements:

- **Python Version**: `Python 3.12.4` is required.
- **Cisco DevNet Sandbox**: Access to Cisco DevNet device is needed.
- **PyATS**: Cisco's test automation platform for network tasks.

---

## Setup Instructions

Follow these steps to set up the project environment:

### Step 1: Create a Virtual Environment
```bash
python3 -m venv .netbot
```

### Step 2: Activate Virtual Environment
```bash
source .netbot/bin/activate
```

### Step 3: Upgrade Pip and Install Dependencies
```bash
python -m pip install --upgrade pip setuptools wheel
pip install --no-cache-dir "pyats[full]"
```


