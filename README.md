<img align="center" src="Images/Gemini_Generated_Image.png" width="100%" height="200" style="object-fit: cover"/>

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

View the interactive Power BI dashboard.

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

- **Microsoft Power BI**: Primary tool for building interactive dashboards and data visualization. 
- **Power BI Service**: Cloud-based sharing and collaboration platform for the final dashboard.
- **Power Query (M Language)**: Used for the **ETL process** (Extract, Transform, Load) to clean and structure raw CSV data.
- **DAX (Data Analysis Expressions)**: Used to create dynamic **Calculated Measures and KPIs** that respond to filters.
- **Python**: Supporting module for **OCR (Optical Character Recognition)** to extract data from unstructured reports.
- **GeoJSON & Custom Maps**: Custom geospatial boundaries defined in `Map-File.json` for precise visual analysis.
- **GitHub**: Used for image hosting (logos/flags) and robust version control.

---

## 🧠 Workflow & Logic

### 1. Data Processing (ETL)
The original Global Terrorism Database (GTD) contains hundreds of columns. Using **Power Query**, we filter this down to essential analytical dimensions:
- **Spatial:** Country, Region, City, Latitude, Longitude.
- **Temporal:** Year, Month, Day.
- **Impact:** Fatalities, Wounded, Property Damage.
- **Categorical:** Attack Type, Target Type, Terrorist Organization.

### 2. Analytical Logic (DAX)
We use custom DAX measures to ensure performance and accuracy:
- **Dynamic KPIs:** Measures that calculate totals based on active slicer selections (e.g., `Total Fatalities = SUM(Terror[nkill])`).
- **Trend Analysis:** Logic to compare year-over-year changes in activity.

### 3. Geospatial Mapping
Logic integrates `Map-File.json` with coordinate data to provide a drill-down experience from **Global → Regional → Local** levels.

---

---

## 📂 Repository Structure

```text
Global-Terrorism-Analysis/
├── 📁 Images/                 # Project screenshots and organization logos
├── 📁 Ocr-Input/              # Raw input files for OCR processing
├── 📁 Ocr-Output/             # Extracted data in CSV format
│
├── 🧠 OCR Logic (Python)
│   ├── Ocr-Extract.py         # Automated data extraction script
│   └── requirements.txt       # Python dependencies
│
├── 📊 Power BI Workspace
│   ├── Terror.pbix            # Main Interactive Dashboard
│   ├── UncleanedTerror.pbix   # Initial Workspace (Ignored by Git)
│   └── Map-File.json          # Custom Geospatial Config
│
├── 📄 Datasets (CSV)
│   ├── Terror.csv             # Processed Dataset
│   ├── CountryFlags.csv       # Flag URL mappings
│   ├── TerroristOrganization.csv # Metadata
│   └── UncleanedTerror.csv    # Raw Data (Ignored by Git)
│
└── 📖 Documentation
    ├── Project-Working-Details.txt # Technical Workflow Details
    └── README.md                   # Main Project Guide
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

## 🔄 Full Project Lifecycle

1.  **Data Ingestion:** Raw datasets (GTD) and OCR-extracted incident data are loaded.
2.  **Transformation:** Power Query cleans nulls, formats dates, and standardizes group names.
3.  **Modeling:** Relationships are established between the main dataset and metadata files like `CountryFlags.csv`.
4.  **Visualization:** Interactive reports are built using maps, trend lines, and KPI cards.
5.  **Interaction:** Users filter data via slicers and drill-through to specific incidents or regions.

---

## 📝 Detailed Documentation
For a deep dive into the specific logic and code implementation, please refer to the technical documentation:
📄 **[Project-Working-Details.txt](Project-Working-Details.txt)**

---

---

## 🧠 OCR Processing (Supporting Module)

The project includes an OCR-based module to extract structured data from unstructured reports or images (like `incident.png`). This allows for local verification of incident details before they are integrated into the main dashboard.

### Workflow

1. **Input:** Place incident images in `Ocr-Input/`.
2. **Execution:** Run the script using `python Ocr-Extract.py`.
3. **Output:** Structured data is saved to `Ocr-Output/IncidentExtracted.csv`.

**Dependencies:** Requires `pytesseract`, `opencv-python`, and `pandas` (listed in `requirements.txt`).

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
