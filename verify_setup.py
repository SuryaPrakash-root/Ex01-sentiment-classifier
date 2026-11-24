#!/usr/bin/env python3
"""
Verify_Setup.py - Verify Development Environment Setup
"""
import os
import sys

import importlib
import subprocess
from pathlib import Path

def check_python_version():
    """Verify Python Version"""
    if sys.version_info[0] >=3.11:
        print(f"Python {sys.version_info[0]} detected")
    elif sys.version_info[0] >=3.11:
        print(f"Python {sys.version_info[0]} detected, Upgrade to Python 3.11 or Higher")
        sys.exit(1)
    pass

def check_virtual_environment():
    """Verify Virtual Environment"""
    if sys.prefix != sys.base_prefix:
        pass
    else:
        print(f"Virtual Environment detected at {sys.base_prefix}")
    pass

def check_required_packages():
    """Verify required packages"""
    required_packages = [
        "torch",
        "transformers",
        "pandas",
        "black",
        "mypy"

    ]
    missing = []
    for package in required_packages:
        if package not in sys.modules:
            try:
                importlib.import_module(package)
                pass
            except ModuleNotFoundError:
                missing.append(package)
                print(f"Package {package} not found, skipping")
    if missing:
        print(f"\nMissing {len(missing)} package(s): {', '.join(missing)}")
        print("Install them with:")
        print(f"  pip install {' '.join(missing)}")
    else:
       pass

    return missing
def check_project_structure():
    """Verify project structure"""
    required_dirs = [
        "src",
        "tests",
        "data",
        "models",
        "configs"
    ]

    required_files = [
        "requirement.txt",
        "requirements-dev.txt",
        ".gitignore",
        ".env.example"
    ]

    missing = []
    for dir in required_dirs:
        if dir not in sys.path:
            missing.append(dir)
    for files in required_files:
        if files not in sys.path:
            missing.append(files)
    pass

def is_git_repo() -> bool:
    """Check if the current directory is inside a Git work tree."""
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True, text=True, timeout=10,
        )
        return out.returncode == 0 and out.stdout.strip() == "true"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def check_git_setup():
    """Verify Git Setup"""
    if not is_git_repo():
        print("FAIL: not a Git repository")
        return False
    #print("Git repo detected")
    return has_venv_ignore()

def has_venv_ignore(gitignore_path: str = ".gitignore") -> bool:
    path = Path(gitignore_path)
    if not path.exists():
        print(f"{gitignore_path} not found")
        return False

    for line in path.read_text().splitlines():
        line = line.strip()
        # skip comments and blank lines
        if not line or line.startswith("#"):
            continue
        # matches "venv/", "/venv", "venv" (bare directory also covers venv/)
        if line in ("venv/", "/venv", "venv"):
            #print(f"OK: found '{line}' in {gitignore_path}")
            return True

    print(f"FAIL: 'venv/' not found in {gitignore_path}")
    return False


def main():
    print("Verifying Development Environment Setup")
    print("=" * 50)

    check = [
        ("Python Version", check_python_version),
        ("Virtual Environment", check_virtual_environment),
        ("Required Packages", check_required_packages),
        ("Project Structure", check_project_structure),
        ("Git Configuration", check_git_setup),
    ]

    all_passed = True

    for check_name, check_func in check:
        try:
            result = check_func()
            if result is False:
                print(f"𐄂 {check_name}")
                all_passed = False
            else:
                print(f"✔ {check_name}")
        except Exception as e:
            print(f"𐄂 {check_name}: {e}")
            all_passed = False
    print("=" * 50)
    if all_passed:
        print("All Checks Passed! Environment is Ready")
        return 0
    else:
        print("Some Checks Failed! Environment is NOT Ready")
        return 1
if __name__ == "__main__":
    sys.exit(main())