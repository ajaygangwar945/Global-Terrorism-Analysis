import os
import sys
import re
import cv2
import pandas as pd
import pytesseract
import shutil

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ---------------- ROBUST PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "Ocr-Input", "incident.png")
OUTPUT_DIR = os.path.join(BASE_DIR, "Ocr-Output")
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "IncidentExtracted.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

if not os.path.exists(IMAGE_PATH):
    print(f"[ERROR] incident.png not found at: {IMAGE_PATH}")
    sys.exit(1)

# ---------------- TESSERACT CONFIGURATION ----------------
if not shutil.which("tesseract"):
    windows_tesseract_paths = [
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Tesseract-OCR\tesseract.exe"),
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        r"C:\Users\ajayg\AppData\Local\Programs\Tesseract-OCR\tesseract.exe",
    ]
    for path in windows_tesseract_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            break

# ---------------- IMAGE PREPROCESSING ----------------
img = cv2.imread(IMAGE_PATH)
if img is None:
    print(f"[ERROR] Could not read image at: {IMAGE_PATH}")
    sys.exit(1)

# Upscale image for clearer text character definition
img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Otsu's automatic thresholding for robust binarization
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ---------------- OCR EXTRACTION ----------------
text = pytesseract.image_to_string(thresh, config="--psm 6").lower()
print("\n--- OCR TEXT ---")
print(text)

# ---------------- REGEX EXTRACTIONS ----------------

# 1. Year Extraction (1900-2099)
year_match = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
year = year_match[0] if year_match else None

# 2. Date Extraction (Supports Month DD, DD Month, MM/DD/YYYY, or 9/11 notation)
MONTHS_PATTERN = r"(?:january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)"
date_patterns = [
    # Month DD, YYYY or Month DD (e.g. "september 11", "september 11, 2001")
    rf'\b{MONTHS_PATTERN}\s+\d{1,2}(?:st|nd|rd|th)?(?:,?\s+\d{2,4})?\b',
    # DD Month YYYY or DD Month (e.g. "11 september 2001")
    rf'\b\d{1,2}(?:st|nd|rd|th)?\s+{MONTHS_PATTERN}(?:,?\s+\d{2,4})?\b',
    # DD/MM/YYYY or MM/DD/YYYY
    r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',
    # Shorthand 9/11
    r'\b9/11\b'
]

date = None
for pattern in date_patterns:
    match = re.search(pattern, text)
    if match:
        date = match.group(0).title()
        break

# 3. Standardized Group Mapping (Matches Terror.csv gname)
GROUP_MAP = {
    r"\b(isis|isil|daesh|islamic state of iraq and the levant)\b": "Islamic State of Iraq and the Levant (ISIL)",
    r"\b(al-qaeda|al qaeda|al-qaida|al qaida)\b": "Al-Qaida",
    r"\b(taliban)\b": "Taliban",
    r"\b(lashkar-e-taiba|let)\b": "Lashkar-e-Taiba (LeT)",
    r"\b(jaish-e-mohammed|jem)\b": "Jaish-e-Mohammed (JeM)",
    r"\b(boko haram)\b": "Boko Haram",
    r"\b(hamas)\b": "Hamas (Islamic Resistance Movement)",
    r"\b(hezbollah|hizballah)\b": "Hezbollah",
    r"\b(farc|revolutionary armed forces of colombia)\b": "Revolutionary Armed Forces of Colombia (FARC)",
    r"\b(eln|national liberation army of colombia)\b": "National Liberation Army of Colombia (ELN)",
    r"\b(shining path|sendero luminoso)\b": "Shining Path (SL)",
    r"\b(maoist|cpi-maoist|communist party of india - maoist)\b": "Communist Party of India - Maoist (CPI-Maoist)",
    r"\b(ulfa|united liberation front of assam)\b": "United Liberation Front of Assam (ULFA)",
    r"\b(ltte|liberation tigers of tamil eelam|tamil tigers)\b": "Liberation Tigers of Tamil Eelam (LTTE)",
    r"\b(eta|basque fatherland and freedom)\b": "Basque Fatherland and Freedom (ETA)",
    r"\b(abu sayyaf|asg)\b": "Abu Sayyaf Group (ASG)",
    r"\b(milf|moro islamic liberation front)\b": "Moro Islamic Liberation Front (MILF)",
    r"\b(bifm|bangsamoro islamic freedom movement)\b": "Bangsamoro Islamic Freedom Movement (BIFM)",
    r"\b(chechen rebels)\b": "Chechen Rebels",
    r"\b(baloch republican army|bra)\b": "Baloch Republican Army (BRA)",
    r"\b(houthi|ansar allah)\b": "Houthi extremists (Ansar Allah)",
}

group = None
for pattern, standardized_name in GROUP_MAP.items():
    if re.search(pattern, text):
        group = standardized_name
        break

# 4. Attack Type Mapping (Supports plurals, verbs, and variations)
ATTACK_MAPPINGS = {
    r"\b(suicide attack(s)?|suicide bomb(ing|ings|er|ers)?)\b": "Suicide Attack",
    r"\b(hijack(ing|ed|er|ers|s)?)\b": "Hijacking",
    r"\b(bomb(ing|ings|ed|s)?|explosion(s)?|car bomb(s)?|improvised explosive)\b": "Bombing/Explosion",
    r"\b(armed assault(s)?|shooting(s)?|gunfire|gunmen|gunman)\b": "Armed Assault",
    r"\b(assassinat(ion|ions|ed)?)\b": "Assassination",
    r"\b(kidnap(ping|pings|ped)?|hostage taking|hostage)\b": "Hostage Taking (Kidnapping)",
    r"\b(grenade attack(s)?)\b": "Bombing/Explosion",
    r"\b(facility/infrastructure attack|arson)\b": "Facility/Infrastructure Attack",
}

attack = None
for pattern, standardized_attack in ATTACK_MAPPINGS.items():
    if re.search(pattern, text):
        attack = standardized_attack
        break

# 5. Countries
COUNTRIES = {
    "united states": "United States",
    "usa": "United States",
    "india": "India",
    "pakistan": "Pakistan",
    "afghanistan": "Afghanistan",
    "iraq": "Iraq",
    "syria": "Syria",
    "nigeria": "Nigeria",
    "philippines": "Philippines",
    "yemen": "Yemen",
    "somalia": "Somalia",
    "colombia": "Colombia",
    "peru": "Peru",
    "united kingdom": "United Kingdom",
    "uk": "United Kingdom",
    "russia": "Russia",
    "france": "France",
    "spain": "Spain",
    "israel": "Israel",
    "palestine": "Palestine",
    "sri lanka": "Sri Lanka",
    "egypt": "Egypt",
    "libya": "Libya",
    "ukraine": "Ukraine"
}

country = None
for name, std_country in COUNTRIES.items():
    if re.search(rf"\b{re.escape(name)}\b", text):
        country = std_country
        break

# 6. Cities
CITIES = [
    "mumbai", "delhi", "srinagar", "karachi", "lahore",
    "baghdad", "kabul", "damascus", "gaza",
    "london", "paris", "new york", "bogota",
    "colombo", "madrid", "manila", "beirut", "arlington"
]

city = None
for c in CITIES:
    if re.search(rf"\b{re.escape(c)}\b", text):
        city = c.title()
        break

# ---------------- FINAL DATAFRAME & CSV EXPORT ----------------
df = pd.DataFrame([{
    "Year": year if year else "null",
    "Date": date if date else "null",
    "GroupName": group if group else "null",
    "AttackType": attack if attack else "null",
    "Country": country if country else "null",
    "City": city if city else "null"
}])

df.to_csv(OUTPUT_CSV, index=False)

print("\n--- EXTRACTED FEATURES (FINAL) ---")
print(df)
print(f"[OK] {os.path.basename(OUTPUT_CSV)} updated successfully at: {OUTPUT_CSV}")
