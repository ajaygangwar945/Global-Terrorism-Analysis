<img align="center" src="Images/Gemini_Generated_Image.png" width="100%" height="200px"/>

<h1 align="center">🌍 Global Terrorism Analysis Dashboard (Power BI)</h1>

<div align="center">

![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Data Analysis](https://img.shields.io/badge/Data-Analytics-4CAF50?style=for-the-badge&logo=databricks&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-Measures-512BD4?style=for-the-badge&logo=microsoft&logoColor=white)
![Geospatial Analysis](https://img.shields.io/badge/Geospatial%20Analysis-Squillion%20%7C%20TMap-0078D4?style=for-the-badge&logo=googlemaps&logoColor=white)
![Dataset](https://img.shields.io/badge/Dataset-GTD-orange?style=for-the-badge&logo=kaggle&logoColor=white)

</div>

---

## 🔎 Project Overview

<div align="left">

<img src="https://img.shields.io/badge/Status-Completed-2EA44F?style=for-the-badge&logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/Maintained-Yes-0969DA?style=for-the-badge&logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/Category-Data%20Analytics-6F42C1?style=for-the-badge&logo=powerbi&logoColor=white" />

</div>

<p align="justify">
  
This project presents an interactive <b>Power BI dashboard</b> built using the <b>Global Terrorism Database (GTD)</b> to analyze worldwide terrorism incidents. It uncovers meaningful patterns and trends across <b>years, regions, countries, attack types, terrorist organizations, and casualties</b>, enabling data-driven insights through rich and interactive visualizations.

</p>

<p align="justify">
The dashboard supports dynamic exploration using slicers, maps, KPIs, and drill-through analysis.
</p>

---

## 🚀 Live Dashboard

View the interactive Power BI dashboard:

[![View Dashboard](https://img.shields.io/badge/Power%20BI-View%20Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://app.powerbi.com/view?r=eyJrIjoiNTY4YWQxMGItNGFhMC00ZWQ4LThlZjUtMDY0NWY4OGJkYjdhIiwidCI6ImUxNGU3M2ViLTUyNTEtNDM4OC04ZDY3LThmOWYyZTJkNWE0NiIsImMiOjEwfQ%3D%3D)

---

## 🧩 Key Features

- 🌍 Interactive geospatial analysis using **Map by Squillion**, **TMap**, **Filled Map**, and **Maps**
- 🖼️ Dynamic terrorist organization logos using **GitHub RAW image URLs**
- 📊 KPI cards displaying **Total Attacks, Fatalities, and Wounded**
- 📈 Year-wise trend analysis of terrorist activities
- 🎛️ Page navigation using **buttons and bookmarks**
- 🔍 Advanced slicers for region, year, country, attack type, and organization
- 🔎 Drill-through pages for detailed analysis

---

## 🛠️ Tools & Technologies

- Microsoft Power BI Desktop  
- Power BI Service  
- Power Query (ETL & Data Cleaning)  
- DAX (Calculated Measures & KPIs)  
- Geospatial Visualization (Map by Squillion, TMap, Filled Map)  
- CSV Datasets  
- GitHub (Image Hosting & Version Control)

---

## 📂 Repository Structure

```
Global-Terrorism-Analysis/  
├── Images/                         # Dashboard screenshots  
├── Ocr-Input/                      # OCR input files  
├── Ocr-Output/                     # OCR extracted output  
│  
├── CountryFlags.csv                # Country–flag mapping  
├── Map-File.json                   # Custom map configuration  
├── Ocr-Extract.py                  # OCR extraction script  
├── README.md                       # Project documentation  
├── Terror.pbix                     # Cleaned Power BI dashboard  
├── UncleanedTerror.pbix            # Raw / uncleaned dashboard  
├── TerrorCSV.zip                   # Terrorism incidents dataset  
└── TerroristOrganizationCSV.zip    # Organization dataset  
```

---

## 📸 Dashboard Screenshots

### 🖥️ Overview Page

<p align="center">
  <img src="Images/Overview.png" width="700"/>
</p>
<p align="center"><i>High-level summary of global terrorism data showing total attacks, fatalities, wounded, and key KPIs</i></p>

### 🌍 Global Terrorism Analysis

<p align="center">
  <img src="Images/Global%20Terrorism%20Analysis.png" width="700"/>
</p>
<p align="center"><i>Global distribution of terrorist attacks with region-wise and country-wise filtering using interactive maps</i></p>

### 🇮🇳 Terrorism in India

<p align="center">
  <img src="Images/Terrorism%20in%20India.png" width="700"/>
</p>
<p align="center"><i>India-specific analysis highlighting state-wise attack patterns, yearly trends, and impact assessment</i></p>

### 🧠 Terrorist Organization Analysis

<p align="center">
  <img src="Images/Terrorist%20Organization%20Analysis.png" width="700"/>
</p>
<p align="center"><i>Organization-wise analysis showing involvement of major terrorist groups and their impact across regions</i></p>

---

## ▶️ How to Use

1. Download the `Terror.pbix` file from the repository  
2. Open it using **Power BI Desktop**  
3. Use slicers to filter by year, region, country, or organization  
4. Navigate between pages using buttons and bookmarks  
5. Explore detailed insights using drill-through features  

---

## 🧠 OCR Processing (Supporting Module)

An OCR-based preprocessing module is included to extract and structure uncleaned textual data before dashboard creation.

- `Ocr-Input/` contains raw input files  
- `Ocr-Output/` stores extracted structured data  
- `Ocr-Extract.py` performs OCR-based extraction and cleaning  

This step helped improve data quality prior to visualization.

---

## 📊 Dataset Information

- **Dataset Name:** Global Terrorism Database (GTD)  
- **Source:** Kaggle  
- **Original Maintainer:** National Consortium for the Study of Terrorism and Responses to Terrorism (START), University of Maryland  
- **Time Period Covered:** 1970 – 2017  
- **File Format:** CSV  

---

## 📌 Learning Outcomes

- Hands-on experience with large real-world datasets  
- Data cleaning, transformation, and modeling using Power Query  
- Designing interactive dashboards and visual storytelling  
- Writing DAX measures for KPIs and analytical insights  
- Publishing and sharing dashboards using Power BI Service  
- Integrating GitHub-hosted assets into Power BI dashboards  

---

## 📚 References

- Global Terrorism Database (GTD): <https://www.kaggle.com/datasets/START-UMD/gtd>  
- Power BI Documentation: <https://learn.microsoft.com/power-bi>  
  
---

⭐ *Feel free to explore the dashboard and repository. Feedback and suggestions are welcome!*
