# AI Document Assistant & Water Quality Dashboard

## Overview

This project is a Streamlit-based Python application developed as part of the **Internship Ready: Software Development** coursework.  
It demonstrates the integration of **data visualization**, **API usage**, and **AI-powered document analysis** in a single interactive web application.

The project consists of two main components:

1. **AI Document Assistant** – Allows users to upload a document and ask questions about its contents using Google’s Gemini AI.
2. **Water Quality Dashboard** – Visualizes environmental data from Biscayne Bay and displays descriptive statistics and plots.

---

## Project Purpose

The goal of this project is to:

- Practice building interactive web applications using **Streamlit**
- Work with real-world datasets using **Pandas**
- Create data visualizations using **Plotly**
- Integrate external APIs (Google Gemini AI and NASA APOD)
- Demonstrate beginner-level software design, modular code structure, and API usage

This project is intended for learning purposes and academic evaluation.

---

## Dataset Used

### Biscayne Bay Water Quality Dataset

- **File:** `biscayneBay_waterquality.csv`
- **Description:**  
  This dataset contains water quality measurements collected from Biscayne Bay, Florida.
- **Key Variables Include:**
  - Time
  - Temperature (°C)
  - pH
  - Dissolved Oxygen (ODO mg/L)
  - Latitude & Longitude
  - Total Water Column (m)

The dataset is used to generate:
- Raw data tables
- Descriptive statistics
- 2D and 3D visualizations

---

## Features

### AI Document Assistant
- Upload a **PDF or TXT** document
- Ask natural language questions about the uploaded document
- AI responds **only using the content of the uploaded file**
- Uses Google Gemini API

### Water Quality Dashboard
- View raw data and summary statistics
- Interactive line, scatter, and 3D plots
- Organized tabs for easy navigation
- Includes NASA’s Astronomy Picture of the Day (APOD) via API

---

## Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **Google Gemini API**
- **NASA APOD API**
- **dotenv** for environment variable management

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
