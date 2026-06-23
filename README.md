# Structural AI Inspection System
AI-powered structural inspection system for detecting defects from images and sensor data, generating engineering reports, and recommending repair priority using computer vision, RAG, and LLM agents.

## Dataset
- Dataset: StructDamage: A Large Scale Unified Crack and Surface Defect Dataset for Robust Structural Damage Detection
- Authors: Misbah Ijaz, Saif Ur Rehman Khan, Abd Ur Rehman, Sebastian Vollmer, Andreas Dengel, Muhammad Nabeel Asim
- License: CC BY 4.0 according to the dataset paper.
- Source: Official DFKI Cloud dataset link from the paper's Data Availability section.
- This project uses StructDamage for research and portfolio demonstration only. The dataset itself is not redistributed in this repository.


## Project Structure

- `apps/web`: Next.js frontend
- `apps/api`: FastAPI backend
- `ml`: model training, evaluation, inference, data, notebooks, and configs
- `rag`: ingestion, retrieval, prompts, and RAG evaluations
- `agents`: repair-priority agent and tools
- `ops`: Docker, Kubernetes, monitoring, and GitHub Actions placeholders
- `docs`: architecture, MLOps, LLMOps, model/data cards, and risk notes


