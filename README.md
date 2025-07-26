# 🌎 Earth911 LLM-Based Scraper

This project is a short technical task that demonstrates how to build a basic LLM-powered scraper for extracting recycling facility data from the Earth911 public directory using OpenAI's API and Python.

---

## ✅ Task Objective

Use OpenAI's LLM (GPT-4) to parse and classify recycling center data from Earth911:
- Search: **Electronics**
- Zip Code: **10001**
- Radius: **Within 100 miles**
- Extract at least 3 entries

---

## 📦 Output Format

Each JSON entry includes:

```json
{
  "business_name": "Example Recycling Center",
  "last_update_date": "2023-11-04",
  "street_address": "123 Main St, NY 10001",
  "materials_category": ["Electronics"],
  "materials_accepted": [
    "Computers, Laptops, Tablets",
    "Small Appliances (Microwaves, Toasters, etc.)"
  ]
}


##Technologies Used
Python 3.10+

OpenAI GPT-4 API

BeautifulSoup

Regex

JSON

##📊 Prompting Strategy
LLMs are used to classify semi-structured material descriptions into predefined categories:

Given raw accepted material text (e.g. “Computers, CRT TVs, Microwaves”)

Prompt asks GPT-4 to match against a list of valid materials under known categories

Outputs clean JSON with materials_category and materials_accepted

Prompt ensures:

Structured output

Multi-label mapping

Strict matching (e.g., "Laptops" → "Computers, Laptops, Tablets")

##🧠 How Edge Cases Are Handled
Scenario	Strategy
Nested/complex HTML	Parsed using BeautifulSoup
JS-rendered data	Simulated with pre-saved HTML (can use Playwright for real pages)
Inconsistent material names	GPT-4 standardizes them into known taxonomy
Missing fields	Regex fallback or default placeholder



##📥 Installation
git clone https://github.com/YOUR_USERNAME/earth911-llm-scraper.git
cd earth911-llm-scraper
pip install -r requirements.txt

##🚀 Run Script

python earth911_scraper.py
##Make sure to:

##Replace "YOUR_OPENAI_API_KEY" with your actual key in the script.
