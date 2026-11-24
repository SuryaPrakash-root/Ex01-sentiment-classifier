#!/bin/bash
# Setup.sh - Automated Environment Setup script
set -e # Exit on error

echo "======================================="
echo "Setting Up Sentiment Classifier Project"
echo "======================================="

echo "Checking Python Version"
python --version

echo "Checking Virtual Environment"
if [ -d "venv" ]; then
  echo "Virtual Environment Already Exists."
  read -p "Recreate it? (y/N)" -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Removing existing virtual environment..."
    rm -rf venv
  fi
fi

#Creating Virtual Environment
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python -m venv venv
fi

#Activation Virtual Environment
echo "Activating Virtual Environment..."
source venv/bin/activate

#Upgrading pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

#Install dependencies
echo "Installing Dependencies"
pip install -r requirements-dev.txt

#Creating .Env from Template if does not exists
if [ ! -f ".env" ]; then
  echo "Creating .env from template"
  cp .env.example .env
  echo "WARNING: .env created from template. Please update with actual value!"
fi

#Run Verification
echo ""
echo "========================================="
echo "Setup complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo "1. Activate environment: source venv/bin/activate"
echo "2. Update .env with your configuration"
echo "3. Run tests: pytest tests/"
echo ""
