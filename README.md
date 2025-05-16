# CI with GitHub Actions Demo

This repository is for exercise 7 in DevOps course, and demonstrates **Continuous Integration** using **GitHub Actions**, featuring:

## Workflows

1. **Basic CI Workflow**  
   Runs on `push` and `pull_request` to `main`.  
   - Checks out code.
   - Runs Python `unittest`.

2. **Matrix Strategy Workflow**  
   Tests on **multiple Python versions (3.9, 3.11, 3.12)** and **OS (Ubuntu, Windows)**.

3. **Daily Scheduled Build**  
   Runs **daily at midnight UTC**, logging a success message.

## Tests

Located in `test_main.py`, validating `compute_mean` from `main.py`.

## How to Trigger the workflows

- **Push / PR to `main`**: Triggers CI workflows.
- **Daily Schedule**: Runs automatically at midnight UTC.
