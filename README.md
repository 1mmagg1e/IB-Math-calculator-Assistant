# IB Math AA SL - TI-84 Calculator AI Guide

This is a AI Chatbot that is specifically for answering questions realted to using the TI-84 calculator for the IB MATH AA SL course. This chatbot can answer student's questions along with visual directions. 

## 📌 Overview

This project provides an intelligent, bilingual conversational AI assistant tailored for IB Mathematics Analysis & Approaches (AA SL). It helps students bridge the gap between mathematical concept extraction and actual TI-84 Graphing Calculator operations.

By leveraging LLM logic combined with an optimized **Image Dictionary Architecture**, the assistant automatically matches calculator keystroke steps with corresponding screen/button screenshots in real time.

## ✨ Key Features

* **3-Step Problem Solving Framework**:
  1. **Identify Variables**: Extracts numerical parameters ($n, p, \mu, \sigma$, etc.) from user prompts.
  2. **Function Mapping**: Identifies exact TI-84 functions (e.g., `binompdf`, `Normalcdf`, `TVM Solver`).
  3. **Keystroke Guide & Visual Integration**: Delivers ordered keystroke instructions alongside automatic screenshot embeds.
* **Proactive Visual Search (System-Level Image Dictionary)**: Embedded image dictionary mapping Markdown assets directly to physical calculator buttons/menus without extra RAG lookup latency.
* **Strict Terminology Anchoring**: Supports dynamic English/Chinese language auto-detection while enforcing English IB Math standard terminology (`binompdf`, `Normal Distribution`).
* **Clean Formatting**: Formatted with standard Markdown, clean button tags (`MATH`, `VARS`), and strict Unicode math operator compliance.

## 🛠️ Tech Stack

* **LLM Engine**: Google Gemini 2.5 Flash
* **Orchestration / RAG**: Dify
* **Automation**: Python 3.x (Image Indexing & Markdown Link Generator)
* **Assets**: GitHub Raw CDN for Calculator UI Screenshots


## ⚠️ Disclaimer
This project is an independent educational tool created for learning support.

IB (International Baccalaureate) is a registered trademark of the International Baccalaureate Organization.

TI-84 Plus is a registered trademark of Texas Instruments.

This project is not affiliated with, endorsed by, or sponsored by IBO or Texas Instruments.



