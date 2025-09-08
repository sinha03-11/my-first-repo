import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Netflix dataset
df = pd.read_csv("netflix_titles.csv")

# Show first 5 rows
print("First 5 rows of Netflix dataset:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Count Movies vs TV Shows
print("\nMovies vs TV Shows count:")
print(df['type'].value_counts())

# Plot Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="type", palette="Set2")
plt.title("Movies vs TV Shows on Netflix")
plt.savefig("movies_vs_tvshows.png")   # Save as PNG
plt.show()

# Top 10 countries with most content
top_countries = df['country'].value_counts().head(10)
print("\nTop 10 countries with most content:")
print(top_countries)

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="coolwarm")
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.savefig("top_countries.png")   # Save as PNG
plt.show()

# Content added per year
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year

# Count how many titles were added each year, sorted by year
yearly_content = df['year_added'].value_counts().sort_index()

print("\nContent added per year:")
print(yearly_content)

# Plot
plt.figure(figsize=(12,5))
sns.lineplot(x=yearly_content.index, y=yearly_content.values, marker="o")
plt.title("Content Added to Netflix Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.savefig("content_by_year.png")   # Save as PNG
plt.show()

# Top 10 genres
all_genres = df['listed_in'].dropna().str.split(', ')
genres = [genre for sublist in all_genres for genre in sublist]
genres_series = pd.Series(genres).value_counts().head(10)

print("\nTop 10 Genres on Netflix:")
print(genres_series)

plt.figure(figsize=(10,5))
sns.barplot(x=genres_series.values, y=genres_series.index, palette="magma")
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.savefig("top_genres.png")   # Save as PNG
plt.show()
