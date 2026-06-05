# GitHub Repo Intelligence Platform

## Vision

An AI-powered platform that helps developers quickly understand unfamiliar GitHub repositories by generating onboarding guides and answering repository-specific questions with evidence from the codebase.

---

## Problem Statement

Developers spend significant time understanding new codebases. Important information is spread across README files, source code, configuration files, APIs, and database logic.

This project reduces onboarding time by automatically analyzing repositories and generating structured onboarding documentation.

---

## Target Users

* New developers joining a project
* Open-source contributors
* Engineering managers evaluating repositories
* Students learning from public repositories
* Non-technical stakeholders seeking a high-level understanding

---

## Core Features

### Repository Analysis

* Accept GitHub repository URL
* Clone repository
* Parse relevant files
* Ignore generated and dependency folders

### AI Onboarding Guide

Generate:

* Project Overview
* Tech Stack
* Folder Structure
* Important APIs
* Database Flow
* Recommended Reading Order
* Key Files

### Repository Q&A

Allow users to ask:

* How does authentication work?
* How is the database connected?
* Which file starts the application?
* What are the main APIs?

---

## Evidence-Based Output

Every generated insight should include supporting evidence.

Examples:

* Source file names
* Configuration files
* Dependencies
* Relevant code snippets

---

## Analysis Strategy

### Phase 1: Metadata Extraction

Analyze:

* README.md
* package.json
* requirements.txt
* pyproject.toml
* pom.xml
* build.gradle
* Dockerfile
* docker-compose.yml
* .env.example

Extract:

* Languages
* Frameworks
* Databases
* External services

### Phase 2: Repository Structure Analysis

Analyze:

* Folder hierarchy
* Entry points
* Key files
* Project organization

### Phase 3: RAG Indexing

* Chunk source code
* Generate embeddings
* Store embeddings in ChromaDB
* Retrieve relevant context for questions

### Phase 4: Guide Generation

Generate onboarding guide using extracted metadata and repository insights.

---

## High-Level Architecture

User
↓
Frontend (React)
↓
Backend (FastAPI)
↓
Repository Cloner
↓
Parser
↓
Metadata Extractor
↓
Chunker
↓
Embedding Generator
↓
ChromaDB
↓
LLM
↓
Guide / Answers

---

## Technology Stack

Frontend:

* React
* TailwindCSS

Backend:

* FastAPI

Vector Database:

* ChromaDB

AI:

* Ollama
* Local embedding model

Storage:

* SQLite

---

## Design Principles

1. Evidence-based outputs
2. Consistent report structure
3. Background indexing
4. Cost-efficient analysis
5. Explainable AI responses

---

## V1 Scope

Included:

* Repository indexing
* AI onboarding guide
* Repository Q&A
* Evidence generation

Not Included:

* Authentication
* Team collaboration
* Multi-user workspaces
* Architecture diagram generation
* GitHub OAuth

---

## Future Enhancements

* Architecture diagrams
* Multi-repository analysis
* Pull request understanding
* Dependency risk analysis
* GitHub integration
* Team onboarding workflows
