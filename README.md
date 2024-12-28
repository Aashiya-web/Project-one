# RedBus Web Scraper and Dashboard

This project automates the process of extracting bus route data from the RedBus website and presents it in an interactive Streamlit dashboard. It involves web scraping using Selenium, data storage in MySQL, and visualization through Streamlit.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)


---

## Overview
The project scrapes bus route data from RedBus, stores it in a MySQL database, and displays it in a user-friendly dashboard. Users can filter and view bus details based on route, bus type, price, and ratings.

---

## Features
- **Web Scraping**: Extracts bus information (name, type, departure, arrival, price, etc.) from RedBus.
- **Database Storage**: Data is inserted into a MySQL database for persistence.
- **Interactive Dashboard**: View and filter bus route information using Streamlit.
- **UI Enhancements**: Responsive table views, filters, and detailed data presentation.

---

## Technologies Used
- **Python** (Selenium, Pandas, PyMySQL)
- **MySQL** (Database)
- **Streamlit** (Dashboard Visualization)
- **HTML/CSS** (Custom Streamlit styling)

---

## Setup and Installation
### Prerequisites
- Python 3.8+
- Chrome WebDriver (Ensure it matches your Chrome version)
- MySQL Database

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```
2. Install dependencies:
   ```bash
   pip install selenium pandas pymysql streamlit mysql-connector-python
   ```
3. Download and place Chrome WebDriver in your PATH.
4. Create a MySQL database named `sakila` and import the schema provided.
5. Update MySQL credentials in the Python files if needed.

---

## Usage
### 1. Web Scraping - RedBus Data Extraction
```bash
python scraper.py
```
- Scrapes bus details and inserts them into the MySQL database.

### 2. Launch Streamlit Dashboard
```bash
streamlit run app.py
```
- Opens a dashboard to visualize and filter bus route data.

---

## Project Structure
```
|-- scraper.py               # Web scraping and database insertion
|-- app.py                   # Streamlit dashboard
|-- requirements.txt         # Required dependencies
|-- readme.md                # Project documentation
```

---

## Database Schema
### Table: `bus_routes`
| Column             | Data Type |
|--------------------|-----------|
| route_name         | VARCHAR   |
| route_link         | VARCHAR   |
| busname            | VARCHAR   |
| bustype            | VARCHAR   |
| departing_time     | TIME      |
| duration           | VARCHAR   |
| reaching_time      | TIME      |
| star_rating        | FLOAT     |
| price              | FLOAT     |
| seats_available    | INT       |
| route_id           | INT       |

---


