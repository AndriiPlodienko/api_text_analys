import openai
import re

# API Key
openai.api_key = "AITOKEN"

# Read text from a file
with open("text.txt", "r") as f:
    text = f.read()

# Remove unnecessary characters from the text
text = re.sub('\n+', ' ', text)  # replacing a newline character with a space
text = re.sub('\[[0-9]*\]', '', text)  # remove numbers in square brackets
text = re.sub('[^\w\s]', '', text)  # removing special characters

# Calling the API for text analysis
response = openai.Completion.create(
    engine="davinci",  
    prompt=f"Statistical analysis of the text:\n{text}",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Displaying statistics on the screen
result = response.choices[0].text.strip()
print(result)
