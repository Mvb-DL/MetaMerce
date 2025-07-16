````markdown
# Automated Content Tagging & Knowledge Graph Builder

**Responsible:** Mario von Bassen  
**Start Date:** 2022-09-01  
**Last Change:** _TBD_  
**Status:** In Progress

---

## Table of Contents

1. [Introduction & Use Case](#introduction--use-case)  
2. [General](#general)  
   1. [Project Scope](#project-scope)  
   2. [Background of the Project](#background-of-the-project)  
   3. [Problem Definition](#problem-definition)  
   4. [Solution Approaches](#solution-approaches)  
   5. [Interfaces and Frameworks](#interfaces-and-frameworks)  
   6. [IDEs and Programs](#ides-and-programs)  
3. [Functional Requirements](#functional-requirements)  
4. [Non-Functional Requirements](#non-functional-requirements)  
   1. [General Requirements](#general-requirements)  
   2. [Legal Requirements](#legal-requirements)  
   3. [Technical Requirements](#technical-requirements)  
5. [General Conditions](#general-conditions)  
   1. [Timetable](#timetable)  
   2. [Technical Requirements](#technical-requirements-1)  
   3. [Risk Analyses](#risk-analyses)  
   4. [Quality and Testing](#quality-and-testing)  
6. [Data Situation](#data-situation)  
7. [Definition of Done](#definition-of-done)  
8. [Attachments](#attachments)  
9. [System Overview](#system-overview)  
   1. [Frontend Overview](#frontend-overview)  
   2. [Backend Overview](#backend-overview)  
   3. [Database](#database)  
   4. [Data Pipeline](#data-pipeline)  
10. [Model](#model)  
    1. [OCR & Title Extraction](#ocr--title-extraction)  
    2. [Data Preprocessing](#data-preprocessing)  
    3. [Title vs Description Classification](#title-vs-description-classification)  
    4. [Deep Learning & Logistic Regression Trainings](#deep-learning--logistic-regression-trainings)  
    5. [Binary Classification Summary](#binary-classification-summary)  
    6. [Undersampled & Oversampled Data](#undersampled--oversampled-data)  
    7. [Multiclass Classification](#multiclass-classification)  
    8. [Algorithm Complexity & Category Classification](#algorithm-complexity--category-classification)  
    9. [Important Papers](#important-papers)

---

## Introduction & Use Case

As a first step, the application should independently identify or classify products (possibly also reviews) of a webshop as products and differentiate them from other content elements with the help of an AI model. A web application provides the user interface for uploading content. Next, the application assigns Schema.org meta-tags (Product, Offer, Review) and expands them with meta descriptions. Finally, it constructs a knowledge graph of the webshop’s assortment for analytics and SEO benefits.

---

## General

### Project Scope

Develop an app where users upload webshop content. The system filters input, extracts data, uses ML to:
- Identify products vs. non-products
- Classify product category, features, and values
- Output Schema.org meta-tags and build a knowledge graph of the assortment

### Background of the Project

Search engines need structured data (Schema.org) to understand webpages. This tool simplifies adding structured data for e-commerce hosts to build semantic sites.

### Problem Definition

- Search engines can’t parse page semantics
- Structured data insertion is hard for non-technical hosts
- Complex entity relationships are hidden
- Large assortments become unmanageable
- Out-of-scope products go unnoticed; recommendations fail
- Verifying entity accuracy and completeness is difficult

### Solution Approaches

- Use Schema.org structured data for ML semantic understanding
- User-friendly upload & tagging interface
- Automated knowledge graph visualization
- Graphical product display options
- Recommender systems & anomaly detection leverage structured data
- Structured data improves SEO rich snippets
- Entity-level data enables quick fact verification

### Interfaces and Frameworks

**Interfaces:**
- Frontend ↔ Backend (REST)
- Backend ↔ Database (SQLite/MySQL)
- Backend ↔ ML Model
- Model ↔ Database

**Frameworks:**
- Python (Flask or Django), R for ML
- Frontend: HTML, CSS, JS (Bootstrap/jQuery/React optional)
- ML: NumPy, pandas, scikit-learn, TensorFlow, Keras
- Visualization: Matplotlib, graph libs

### IDEs and Programs

- **Frontend:** VS Code
- **Backend:** PyCharm
- **Model:** Anaconda, Jupyter, PyCharm, Google Colab

---

## Functional Requirements

**Basic Features:**
- User registration, login/logout
- Account management (edit/delete)
- Upload code, images, HTML/text
- Save user data and settings
- Download/copy model output

**Extended Features:**
- Social media sharing
- Reviews & voting
- Google Mail integration
- Activity tracking
- Notifications & updates
- Account status dashboard

---

## Non-Functional Requirements

### General Requirements

- **Loading Time:** ≥ 90 on Google Lighthouse
- **Usability:** Follow Nielsen’s 10 heuristics; usability testing
- **Responsive Design:** Desktop-first; support mobile/tablet

### Legal Requirements

- GDPR/Data Protection Act compliance
- Cookie consent (Google Analytics)

### Technical Requirements

- Cross-browser: Chrome, Safari, Edge, Firefox, Opera

---

## General Conditions

### Timetable

- **Duration:** 2022-09-01 to 2023-01-31
- **Effort:** ≥ 40 hours/week

### Technical Requirements

- Access to Google Colab & Jupyter Notebook
- Hardware: laptop for mobile work; tower PC for model training

### Risk Analyses

_See risk table in attachments._

### Quality and Testing

- Define QA process; use test plans, review cycles

---

## Data Situation

Combined public datasets for product/review classification. After cleaning, obtained:
- **13,172,462** products (as of 2022-09-28) with title, category, brand, description
- Datasets for binary (title vs. description) and multiclass classification

---

## Definition of Done

Specifies deliverables, pricing, timelines, acceptance criteria, and stakeholder responsibilities. Project completes when all functional/non-functional requirements pass QA and stakeholder sign-off.

---

## Attachments

- Detailed specs, diagrams, risk tables, dataset summaries

---

## System Overview

### Frontend Overview

**Functional Requirements:**
- Account CRUD
- Login/registration UI
- Upload & result pages
- Settings page

**Design:** Figures 3–7 (login, upload, result, account settings)

### Backend Overview

Written in Flask (lightweight vs. Django). Uses SQLite (migrate to MySQL later). Supports user and upload data management.

### Database

Entity-Relationship Diagrams (first draft)

### Data Pipeline

1. **Upload:** URL scrape / manual text/HTML / image upload
2. **Storage:** raw data for display & model training
3. **Processing:** text cleaning, OCR, extraction, classification
4. **Output:** display on site or save for model

---

## Model

### OCR & Title Extraction

```python
import easyocr, cv2, numpy as np
# ... sample code to detect largest font regions as title candidates
````

### Data Preprocessing

* Select columns: title, category, brand, description
* Remove special chars, numeric-only rows, HTML tags
* Expand contractions, deduplicate
* Filter by length (title < 30 words, description < 300 words)
* Lowercase, remove stopwords, lemmatize

### Title vs Description Classification

* Binary classification: Title (1) vs. Description (0)
* Under-/oversampling due to class imbalance
* TF‑IDF vs. CountVectorizer; unigram/bigram tests

### Deep Learning & Logistic Regression Trainings

* Multiple training runs (1–11) varying vectorizer, max\_features, n-grams, solver
* Report precision, recall, F1-score, accuracy

### Binary Classification Summary

| Run | Solver    | Vectorizer         | Features | n‑gram | Score |
| --- | --------- | ------------------ | -------- | ------ | ----- |
| 1   | liblinear | CV                 | 1500     | uni    | 92%   |
| …   | …         | …                  | …        | …      | …     |
| 11  | liblinear | TF‑IDF (min\_df=5) | 3500     | uni    | 95%   |

### Undersampled & Oversampled Data

* Undersampled logistic regression runs (mf\_df 1–20); scores \~94.5%
* Oversampling doubles training time with similar scores

### Multiclass Classification

* Four classes: Title, Brand, Category, Description
* Initial imbalance; apply sampling techniques
* Logistic Regression & other algorithms; scores \~80–94%

### Algorithm Complexity & Category Classification

* KNN: brute-force O(knd), KD-tree O(n d log n)
* Category classification uses extracted Title, Brand, Description as inputs

### Important Papers

* *Semantic Web for E‑Commerce*, arXiv:2109.01084
* *Title Classification Techniques*, NTU CSIE

```markdown
```
