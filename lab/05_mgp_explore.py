#%% Basic fetch and parse of a single MGP page
import requests
from bs4 import BeautifulSoup

url = "https://www.mathgenealogy.org/id.php?id=18231"  # David Hilbert
html = requests.get(url, timeout=10).text

#%%



soup = BeautifulSoup(html, "html.parser")

# Print the page title and the first few links
print(soup.title.string)
for a in soup.select("a[href*='id.php?id=']")[:10]:
    print(a.text, "→", a["href"])

#%% Turn that into a dataframe of student names and ids
import pandas as pd
import re

rows = []
for a in soup.select("a[href*='id.php?id=']"):
    name = a.text.strip()
    m = re.search(r"id=(\\d+)", a["href"])
    if m:
        rows.append({"name": name, "mgp_id": m.group(1)})

df = pd.DataFrame(rows)
df.head()

