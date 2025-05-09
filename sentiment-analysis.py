from textblob import TextBlob

# Load first document, the interpretation of dreams
with open("interpretation-dreams.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split by paragraph
paragraphs = text.split('\n\n')

# Analyze
results = []
for i, para in enumerate(paragraphs):
    blob = TextBlob(para)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    results.append((i, polarity))
    results.append((i, subjectivity))

# Save/write output
with open("dreams_scores.csv", "w") as f:
    f.write("Paragraph,Polarity,Subjectivity\n")
    for i, para in enumerate(paragraphs):
        blob = TextBlob(para)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        f.write(f"{i},{polarity},{subjectivity}\n")



# Load second document, three contributions to the theory of sex
with open("three_contributions.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split by paragraph
paragraphs = text.split('\n\n')

# Analyze
results = []
for i, para in enumerate(paragraphs):
    blob = TextBlob(para)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    results.append((i, polarity))
    results.append((i, subjectivity))

# Save/write output
with open("contribution_scores.csv", "w") as f:
    f.write("Paragraph,Polarity,Subjectivity\n")
    for i, para in enumerate(paragraphs):
        blob = TextBlob(para)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        f.write(f"{i},{polarity},{subjectivity}\n")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSVs
dreams = pd.read_csv("dreams_scores.csv")
contrib = pd.read_csv("contribution_scores.csv")

# Add source labels
dreams['Document'] = 'Interpretation of Dreams'
contrib['Document'] = 'Three Contributions'

# Combine data
combined = pd.concat([dreams, contrib])


# Plot: Polarity
plt.figure(figsize=(12, 6))
sns.lineplot(data=combined, x='Paragraph', y='Polarity', hue='Document')
plt.title("Sentiment Polarity per Paragraph")
plt.xlabel("Paragraph Index")
plt.ylabel("Polarity Score")
plt.axhline(0, color='gray', linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

# Plot: Subjectivity
plt.figure(figsize=(12, 6))
sns.lineplot(data=combined, x='Paragraph', y='Subjectivity', hue='Document')
plt.title("Sentiment Subjectivity per Paragraph")
plt.xlabel("Paragraph Index")
plt.ylabel("Subjectivity Score")
plt.axhline(0.5, color='gray', linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("polarity_plot.png")


top_positive = combined.sort_values('Polarity', ascending=False).head(5)
top_negative = combined.sort_values('Polarity').head(5)
top_subjective = combined.sort_values('Subjectivity', ascending=False).head(5)

print(top_positive)
print(top_negative)
print(top_subjective)

with open("interpretation-dreams.txt", "r", encoding="utf-8") as f:
    dreams_paragraphs = f.read().split('\n\n')

with open("three_contributions.txt", "r", encoding="utf-8") as f:
    contrib_paragraphs = f.read().split('\n\n')


for _, row in top_subjective.iterrows():
    para_index = int(row['Paragraph'])
    if row['Document'] == "Interpretation of Dreams":
        para_text = dreams_paragraphs[para_index]
    else:
        para_text = contrib_paragraphs[para_index]
    
    print(f"\n--- Paragraph {para_index} ({row['Document']}) ---")
    print(para_text)



for _, row in top_negative.iterrows():
    para_index = int(row['Paragraph'])
    if row['Document'] == "Interpretation of Dreams":
        para_text = dreams_paragraphs[para_index]
    else:
        para_text = contrib_paragraphs[para_index]
    
    print(f"\n--- Paragraph {para_index} ({row['Document']}) ---")
    print(para_text)

for _, row in top_positive.iterrows():
    para_index = int(row['Paragraph'])
    if row['Document'] == "Interpretation of Dreams":
        para_text = dreams_paragraphs[para_index]
    else:
        para_text = contrib_paragraphs[para_index]
    
    print(f"\n--- Paragraph {para_index} ({row['Document']}) ---")
    print(para_text)
