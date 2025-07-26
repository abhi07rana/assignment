import requests
from bs4 import BeautifulSoup
import openai
import re
import json
from datetime import datetime

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual key

# Step 1: Use Earth911's public search tool manually or simulate search result fetch.
# Due to JS rendering, we simulate this part by hardcoding sample HTML (normally would use Playwright or Selenium).

sample_html = """
<div class="location-result">
    <h3 class="location-name">eRecycleNYC</h3>
    <div class="location-address">460 W 34th St, New York, NY 10001</div>
    <div class="location-materials">
        Accepted: Computers, Monitors, TVs, Cell Phones, Printers, Small Appliances, Cables
    </div>
    <div class="last-update">Last Updated: Nov 04, 2023</div>
</div>
<div class="location-result">
    <h3 class="location-name">Lower East Side Ecology Center</h3>
    <div class="location-address">E 7th St & Avenue B, New York, NY 10009</div>
    <div class="location-materials">
        Accepted: Laptops, Smartphones, Keyboards, CRT TVs, Microwaves
    </div>
    <div class="last-update">Last Updated: Oct 21, 2023</div>
</div>
"""

# Step 2: Parse HTML
soup = BeautifulSoup(sample_html, 'html.parser')
facilities = soup.find_all("div", class_="location-result")

entries = []

for facility in facilities:
    name = facility.find("h3", class_="location-name").text.strip()
    address = facility.find("div", class_="location-address").text.strip()
    raw_materials = facility.find("div", class_="location-materials").text.strip()
    last_updated = facility.find("div", class_="last-update").text.strip()
    
    # Extract date
    last_date_match = re.search(r"Last Updated:\s*(.*)", last_updated)
    last_date = datetime.strptime(last_date_match.group(1), "%b %d, %Y").strftime("%Y-%m-%d") if last_date_match else ""

    # Prompt LLM to classify into categories
    prompt = f"""
Given the following accepted materials: "{raw_materials}", classify them into the predefined materials_category and materials_accepted from this list:

Electronics:
1. Computers, Laptops, Tablets
2. Monitors, TVs (CRT & Flat Screen)
3. Cell Phones, Smartphones
4. Printers, Copiers, Fax Machines
5. Audio/Video Equipment
6. Gaming Consoles
7. Small Appliances (Microwaves, Toasters, etc.)
8. Computer Peripherals (Keyboards, Mice, Cables, etc.)

Respond as a JSON object with keys: materials_category (array), materials_accepted (array).
Only include relevant matches.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    extracted = json.loads(response['choices'][0]['message']['content'])

    entries.append({
        "business_name": name,
        "last_update_date": last_date,
        "street_address": address,
        "materials_category": extracted["materials_category"],
        "materials_accepted": extracted["materials_accepted"]
    })

# Output the final JSON
print(json.dumps(entries, indent=2))
