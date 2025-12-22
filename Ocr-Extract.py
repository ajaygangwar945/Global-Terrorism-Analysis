import pytesseract
import cv2
import pandas as pd
import re
import os

# ---------------- PATHS ----------------
IMAGE_PATH = r"C:\Users\ajayg\College\SEM 5\INT 374\Project\Ocr-Input\incident.png"
OUTPUT_CSV = r"C:\Users\ajayg\College\SEM 5\INT 374\Project\Ocr-Output\IncidentExtracted.csv"

if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError("❌ incident.png not found in Ocr-Input folder")

# ---------------- IMAGE PREPROCESSING ----------------
img = cv2.imread(IMAGE_PATH)
img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

# ---------------- OCR ----------------
text = pytesseract.image_to_string(gray, config="--psm 6").lower()
print("\n--- OCR TEXT ---\n", text)

# ---------------- REGEX EXTRACTION ----------------
year_match = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
year = year_match[0] if year_match else "null"

date_match = re.findall(
    r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b|\b\d{1,2}\s+[a-z]+\s+\d{4}\b',
    text
)
date = date_match[0] if date_match else "null"

# ---------------- STANDARDIZED DICTIONARIES ----------------
GROUP_MAP = {
    "isis": "Islamic State of Iraq and the Levant (ISIL)",
    "isil": "Islamic State of Iraq and the Levant (ISIL)",
    "daesh": "Islamic State of Iraq and the Levant (ISIL)",
    "al qaeda": "Al-Qaida",
    "al-qaeda": "Al-Qaida",
    "al-qaida": "Al-Qaida",
    "taliban": "Taliban",
    "lashkar-e-taiba": "Lashkar-e-Taiba (LeT)",
    "jaish-e-mohammed": "Jaish-e-Mohammed (JeM)",
    "boko haram": "Boko Haram",
    "hamas": "Hamas",
    "hezbollah": "Hizballah",
    "farc": "Revolutionary Armed Forces of Colombia (FARC)",
    "elt": "ELN",
    "shining path": "Shining Path (SL)",
    "maoist": "Communist Party of India - Maoist (CPI-Maoist)",
    "isi": "Inter-Services Intelligence (ISI)"
}

ATTACK_TYPES = [
    "bombing", "explosion", "armed assault", "shooting",
    "suicide attack", "assassination", "kidnapping",
    "hostage taking", "grenade attack", "arson", "hijacking"
]

COUNTRIES = [
    "india", "pakistan", "afghanistan", "iraq", "syria",
    "nigeria", "united states", "philippines",
    "yemen", "somalia", "colombia", "peru"
]

CITIES = [
    "mumbai", "delhi", "srinagar", "karachi", "lahore",
    "baghdad", "kabul", "damascus", "gaza",
    "london", "paris", "new york", "bogota"
]

# ---------------- SAFE MATCHING ----------------
def match_from_list(items, text):
    for item in items:
        if re.search(rf"\b{re.escape(item)}\b", text):
            return item
    return "null"

raw_group = match_from_list(GROUP_MAP.keys(), text)
group = GROUP_MAP.get(raw_group, "null")

attack = match_from_list(ATTACK_TYPES, text)
country = match_from_list(COUNTRIES, text)
city = match_from_list(CITIES, text)

# ---------------- FINAL OUTPUT (NO CONFIDENCE COLUMN) ----------------
df = pd.DataFrame([{
    "Year": year,
    "Date": date,
    "GroupName": group,
    "AttackType": attack.title() if attack != "null" else "null",
    "Country": country.title() if country != "null" else "null",
    "City": city.title() if city != "null" else "null"
}])

df.to_csv(OUTPUT_CSV, index=False)

print("\n--- EXTRACTED FEATURES (FINAL) ---")
print(df)
print("✅ IncidentExtracted.csv updated successfully")
