from hashlib import sha256
import pandas as pd


your_hash = sha256("STU001".encode()).hexdigest()
print(f"SHA-256 hash of 'STU001': {your_hash}")
to_find = your_hash[:8]

# Read reviews.csv
df = pd.read_csv("reviews.csv")

# Ensure 'text' column is string, then search for the hash prefix
matches = df[df['text'].astype(str).str.contains(to_find, case=False, na=False)]

if not matches.empty:
    # Get all matching titles (may be multiple)
    titles = matches['title'].tolist()
    print("Found hash in these title(s):")
    for t in titles:
        print("-", t)
else:
    print("Hash not found in the 'text' column.")
    exit()

title = titles[0]

FLAG1 = sha256(title.replace(" ", "")[:8].encode()).hexdigest()
print(f"FLAG1 = {FLAG1}")

# FLAG2
print(f"FLAG2 = FLAG2{{{to_find.upper()}}}")
