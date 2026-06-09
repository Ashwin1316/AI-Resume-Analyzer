# AI Resume Analyzer

## Overview
AI Resume Analyzer is a Generative AI application that helps job seekers optimize their resumes for specific job descriptions. The system analyzes uploaded resumes, identifies skill gaps, provides ATS-friendly recommendations, and generates personalized interview questions using Large Language Models (LLMs).

## Features
- Resume Parsing and Text Extraction
- Job Description Matching
- ATS Score Analysis
- Skill Gap Identification
- AI-Powered Resume Improvement Suggestions
- Personalized Interview Question Generation
- Retrieval-Augmented Generation (RAG) Support
- REST API Integration using FastAPI
- Docker Deployment Support

## Tech Stack

### Programming Language
- Python

### Frameworks
- FastAPI
- LangChain

### AI & Generative AI
- OpenAI API / Gemini API
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)

### Vector Database
- ChromaDB

### Tools
- Git
- Docker
- Postman

## Project Architecture

User Resume + Job Description
        |
        v
   Resume Parser
        |
        v
   Text Processing
        |
        v
   Vector Embeddings
        |
        v
      ChromaDB
        |
        v
   RAG Retrieval
        |
        v
   LLM Analysis
        |
        v
ATS Score + Skill Gap Analysis
+ Resume Suggestions
+ Interview Questions

## Installation

```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
pip install -r requirements.txt
uvicorn app:app --reload
```

## Resume Description

- Developed an AI-powered resume analysis application using LangChain and LLM APIs to evaluate resumes against job descriptions and identify skill gaps.
- Implemented Retrieval-Augmented Generation (RAG) with ChromaDB to provide contextual ATS optimization suggestions and personalized feedback.
- Built FastAPI-based REST APIs for resume parsing, interview question generation, and automated resume improvement recommendations.

## Future Enhancements
- LangGraph-based Multi-Agent System
- Azure OpenAI Integration
- Resume Ranking Dashboard
- PDF Report Generation
- CI/CD Deployment Pipeline
