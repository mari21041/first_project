
# 🧠 Human Trafficking Data Intelligence: *Modern Day Slavery Still Exists*

> **Human trafficking is not history — it is today’s silent crisis.**  
> This project brings data to the frontlines of one of the world’s most pressing human rights challenges.

---

## 🌍 Project Title: International Trafficking Victim Analytics & Intelligence

### 📣 Executive Summary

This project addresses the global issue of modern-day slavery using data analytics. Human trafficking remains widespread, with many victims going unidentified and unsupported. By analyzing international data, we aim to uncover patterns, highlight countries with significant reports of human trafficking, and assist data-based decisions by governments and NGOs working to stop these crimes and help survivors.

Our project is framed as a **public threat case**, with the goal to:
- **Understand the scope and distribution** of trafficking offenses.
- **Uncover patterns in victim demographics** to inform specialized support.
- **Help governments and NGOs** strategically allocate resources and establish victim recovery centers.

By analyzing reported geographic and demographic data on this issue, we seek to build insights that raise awareness and assist real-world intervention.

---

## 🔍 Hypothesis & Research Questions

### Hypothesis
With the right data, enforcement agencies can identify critical hotspots and demographic groups in need of immediate support. 

Insights:

> Determine the concentration of reported victims and types of trafficking to assist governments make data-based decisions to fight these crimes.

> Assist NGOs as to where (which countries) to open up support centers to help victims.


### Key Questions
- Which countries have the highest number of reported offenses and need prioritized support from NGOs?
- What are the gender and age demographics of victims?

---

## 🧾 Dataset Description

The dataset, comprising of **39485 rows** and **10 columns**, originates from the United Nations Office on Drugs and Crime and encompasses two decades of  multilevel information  data  across **regions**, **subregions**, **countries**, and **demographics**, **victims** and **offenders**.

### Features Breakdown:

| Column           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `country`        | Country where the incident occurred or victim was detected                  |
| `region`         | High-level regional classification (e.g., Asia, Africa)                     |
| `subregion`      | Subdivided region classification                                            |
| `indicator`      | Classification of the record (e.g., offense or victim repatriation)         |
| `dimension`      | Reporting dimension (e.g., country of detection, repatriation)              |
| `category`       | Victim source category or trafficking type                                  |
| `sex`            | Gender of the victim (if reported)                                          |
| `age`            | Age group (minor or adult) (if reported)                                    |
| `year`           | Year the offense or detection was reported                                  |
| `nr_of_victims`  | Number of victims (cleaned and converted to numeric for analysis)           |

> Note: Data cleaning was applied to standardize victim counts and handle anonymized entries (e.g., "<5" to mean value "2.5").

### Dataset obstacles:

In analyzing datasets related to illicit activities, a major challenge is incomplete reporting, leading to missing values. This lack of data, often due to underreporting or the secretive nature of these activities, complicates data processing and analysis. Such gaps can undermine the accuracy of analytical models, requiring techniques like data imputation to mitigate the impact and enhance analysis reliability.

---

## 🧱 Entity Relationship Model and Diagram

The database schema is relationally structured to support multi-layered analysis across geography and time.

### Core Tables:

- **Region (region_id, region_name)**  
- **Subregion (subregion_id, subregion_name, region_id)**  
- **Country (country_id, country_name, subregion_id)**  
- **Victim (victim_id, sex, age)**  
- **Offense (offense_id, year, dimension, category, nr_of_victims, country_id, victim_id)**

### Cardinality Logic:

- Each `Offense` may involve one or more `Victims`.
- Each `Country` has multiple `Offenses`.
- A `Region` contains multiple `Subregions`, which contain multiple `Countries`.


![ER Model](first_project\slides\ERM.png)
![ER Diagram](first_project\slides\ERD.png) 

This normalized schema allows efficient filtering and joins across geography, victim profiles, and offense dimensions.

---

### 📊 Exploratory Data Analysis (EDA)

- **Temporal Trends**: Year-over-year tendencies in reported victims
- **Geospatial Mapping**: Statistics of trafficking victim per country of report
- **Victim Profiling**: Clustering victims by age/sex/type of exploitation

---

## 💻 Technologies Used

| Area                 | Tools/Technologies                                      |
|----------------------|---------------------------------------------------------|
| Data Manipulation    | Python (Pandas, NumPy)                                  |
| Data Visualization   | Matplotlib, Seaborn, Pyplot                             |
| Database Modeling    | MySQL Workbench, Miro, Lucid                            |
| Documentation        | Jupyter Notebook, Markdown, GitHub, Visual Studio Code  |
| Version Control      | Git, GitHub, Anaconda Powershell                        |

---

## 📦 Deliverables

- ✅ [Repository "first_project" on GitHub](https://github.com/mari21041/first_project) 
- ✅ [Raw dataset](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fdataunodc.un.org%2Fsites%2Fdataunodc.un.org%2Ffiles%2Fdata_glotip.xlsx&wdOrigin=BROWSELINK)
- ✅ Jupyter Notebook with cleaned and documented dataset (`load_clean_data.csv`)
- ✅ ERM and ERD schemas with relationship logic
- ✅ Jupyter Notebook with EDA and visualizations
- ✅ MySQL file with data base and quaries
- ✅ README documentation
- ✅ [Final presentation report](https://docs.google.com/presentation/d/1ZxcF3VxB39Q2w0D33H5HTTdKfI78sPBHEtSYHJ0Mm8I/edit?usp=sharing) 

---

## 👨‍💼 Target Audience

- **Policy Makers**: Use insights to influence anti-trafficking strategies
- **NGOs**: Suggest as to where to open possible support centers geographically
- **Researchers**: Access a clean dataset for further academic work

---

## 🛠️ Future Work

- Further research can be done to include perpetrators information (from additional dataset) to create an overall view of both victims and perpetrators.
- The analysis can be deepened into specific trafficking dynamics in each country for more focused enforcement efforts
- Analyze the possibility of using predictive models to complete the "Unknown" values of the reports

---

## 👥 Contributors

- Hipolito Marin  
- Marianne Filbig  
- Delmar Bumanglag  
- Egbe Grace  

---

## 🌐 Call to Action

Human trafficking is real, widespread, and preventable. Data-driven insights must be used to take concrete steps.  
📢 *Share this repository, contribute to awareness, and help make a difference.*

