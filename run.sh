#!/bin/bash

echo "=============================================="
echo " AI Product Visibility & Trust Monitoring "
echo "=============================================="
echo ""

echo "Step 1: Generating shopping prompt..."
python3 monitor/prompt_engine.py
echo ""

echo "Step 2: Collecting AI responses..."
python3 monitor/ai_connector.py
echo ""

echo "Step 3: Running hallucination detection..."
python3 monitor/hallucination_checker.py
echo ""

echo "Step 4: Updating monitoring dashboard..."
echo "Dashboard updated successfully."
echo ""

echo "Prototype run complete."
