# Automated Content Tagging & Knowledge Graph Builder

**Responsible:** Mario von Bassen  
**Start Date:** 2022‑09‑01  
**Last Change:** _TBD_  
**Status:** In Progress  

---

## Table of Contents

1. [Introduction](#introduction)  
2. [Project Scope](#project-scope)  
3. [Background & Problem Definition](#background--problem-definition)  
4. [Solution Overview](#solution-overview)  
5. [Interfaces & Frameworks](#interfaces--frameworks)  
6. [Requirements](#requirements)  
   - [Functional Requirements](#functional-requirements)  
   - [Non‑Functional Requirements](#non-functional-requirements)  
7. [System Architecture](#system-architecture)  
   - [Data Pipeline](#data-pipeline)  
   - [Model Components](#model-components)  
8. [Installation & Usage](#installation--usage)  
9. [Roadmap & Milestones](#roadmap--milestones)  
10. [Definition of Done](#definition-of-done)  
11. [Attachments](#attachments)  

---

## Introduction

This project is a **web application** that automates:

- **Content Identification** — detect products, offers, reviews in any web shop page  
- **Meta‑tagging & Classification** — assign [schema.org](https://schema.org/docs/schemas.html) types (Product, Offer, Review) and generate JSON‑LD  
- **Knowledge Graph Construction** — build a semantic graph of the shop’s assortment for analytics, SEO improvement, up‑/cross‑selling recommendations  

---

## Project Scope

1. **Upload Interface**: Users upload HTML/text/images of their webshop content.  
2. **Data Extraction**: System filters, cleans, and extracts raw data.  
3. **AI Classification**: A trained ML model labels each fragment as Product, Offer, or Review and identifies attributes (brand, category, price, etc.).  
4. **Meta‑tag Generation**: Output structured data JSON‑LD per Schema.org.  
5. **Knowledge Graph**: Visualize and export semantic relationships among products.  

---

## Background & Problem Definition

Many e‑commerce sites lack structured metadata, so search engines can’t fully understand page content.  
**Key challenges**:  
- Unstructured product pages → poor SEO rich snippets  
- Non‑technical site owners struggle to embed structured data  
- Large assortments become unmanageable; up‑/cross‑sell opportunities are missed  

---

## Solution Overview

- **Automated Schema.org Markup** → improves search ranking & enables rich snippets  
- **User‑friendly UI** → drag‑and‑drop uploads, one‑click tagging  
- **Knowledge Graph Dashboard** → visual overview of products & relationships  
- **Recommender & Anomaly Detection** → driven by structured data  
- **Analytics Export** → CSV/JSON/Graph formats for further analysis  

---

## Interfaces & Frameworks

### Interfaces

- **Frontend ↔ Backend** (REST API)  
- **Backend ↔ Database** (SQLite → MySQL support)  
- **Backend ↔ ML Model** (Python/R)  

### Frameworks & Libraries

- **Backend**: Flask (or Django)  
- **Frontend**: HTML/CSS/JS (optional Bootstrap/jQuery/React)  
- **ML & Data**: NumPy, pandas, scikit‑learn, TensorFlow, Keras  
- **Visualization**: Matplotlib, custom graph library  
- **IDE/Notebooks**: VS Code, PyCharm, Jupyter, Google Colab  

---

## Requirements

### Functional Requirements

- **User Management**: sign up, log in/out, update/delete account  
- **Data Upload**: HTML/text/images of products  
- **Meta‑tag Output**: download or copy generated JSON‑LD  
- **Knowledge Graph**: interactive view & export  
- **Social & Notifications**: share results, email updates  

### Non‑Functional Requirements

- **Performance**: Google Lighthouse ≥ 90  
- **Usability**: Nielsen’s 10 heuristics; usability testing  
- **Responsive Design**: desktop‑first, mobile/tablet support  
- **Security & Compliance**: GDPR/Data Protection Act  
- **Browser Compatibility**: Chrome, Safari, Edge, Firefox, Opera  

---

## System Architecture

```plaintext
[ User Browser ] → [ Frontend (Flask/React) ] → [ Backend API ]
                   ↳ [ ML Model Server ]         ↳ [ Database ]
