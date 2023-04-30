# api_text_analys

Code explanation:

    openai.api_key - the API key that was received during registration on the OpenAI website.

    with open("text.txt", "r") as f: - reading text from the file "text.txt".

    re.sub() - function to replace or delete certain characters from the text.

    openai.Completion.create() - call the ChatGPT API to analyze the text.

    response.choices[0].text.strip() - getting the results of the analysis and displaying them on the screen.

When the program is launched, the screen will display statistics on the number of words, sentences, and named entities in the text.
