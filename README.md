# fastapi-ci-cd-finkproject

# FastAPI CI/CD DevOps Project

## Project Overview

This project demonstrates a fully automated, production-ready Continuous Integration and Continuous Deployment (CI/CD) pipeline for a simple FastAPI application. The pipeline is built using **GitHub Actions** and deploys to **Render**, showcasing a modern DevOps workflow from code commit to live deployment.

## Key Features

- **Automated CI/CD Pipeline**: The workflow is triggered automatically on every Pull Request and merge, ensuring code is validated before deployment.
- **Continuous Integration (CI)**:
  - **Code Quality Checks**: Automated linting using `Flake8` to enforce code style.
  - **Automated Testing**: Runs unit tests with `Pytest` to ensure code integrity.
- **Continuous Deployment (CD)**:
  - Deploys the application to a live web service on **Render**.
- **Role-Based Access Control (RBAC)**:
  - Enforces a secure workflow using GitHub Teams (`Dev`, `QA`, `Release`) and branch protection rules.
- **Standardized Workflow**:
  - Utilizes a Pull Request template to standardize contributions and ensure quality.
- **Notifications**:
  - Sends notifications on CI/CD events to a dedicated Slack channel.

## Project Architecture

This project follows a standard branching strategy for a professional development workflow.

1.  **`dev` branch**: Where new features are developed and tested.
2.  **`qa` branch**: A staging environment for quality assurance and final review.
3.  **`release` branch**: A stable branch used for production releases.
4.  **`main` branch**: The production-ready code that is automatically deployed to the live environment.

## The CI/CD Flow

1.  A developer creates a new feature branch and opens a **Pull Request** to the `dev` branch.
2.  **GitHub Actions** automatically runs the **linting** and **testing** jobs.
3.  Once checks pass and a team lead approves, the PR is merged into `dev`.
4.  A PR is created from `dev` to `qa`, then `qa` to `release`, and finally `release` to `main`.
5.  Each merge triggers the automated deployment pipeline to the live environment.

## Technologies Used

- **Framework**: FastAPI
- **CI/CD Platform**: GitHub Actions
- **Cloud Hosting**: Render
- **Version Control**: Git / GitHub
- **Testing**: Pytest
- **Linting**: Flake8
- **Notifications**: Slack
