# Newsscraper
First step to having your LLM parse a live website is to isolate the main text. 
Newsscraper uses the Newspaper import to trim the excess data from your scrape. 
I noticed that my scrapes had previously included a bunch of irrelevant data from the webpage; for example, in addition to the main news article being captured, there were links and info from other ads and previews of posts that made the file much longer and was noise. Trimming the noise out means that the content is much more clearly extracted, and shorter. Shorter text = less tokens used on a GPT API call = more bandwidth or lower cost.  

Console Instructions:

at Command line, User input: website URL to crape data from, and FILENAME to save data to

NEWSSCRAPER Program scrapes the main text from the website and save a JSON file:

# Create a dictionary with the extracted data
data = {
    "website": website_url,
    "timestamp": str(datetime.now()),
    "text": extracted_text
}

