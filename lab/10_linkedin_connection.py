#%%
import webbrowser
import urllib.parse

#%% Test query for LinkedIn search
query = "Patrick Clarke math PhD"

#%% LinkedIn search for a person
query = "Patrick Clarke math PhD"
# Option 1: LinkedIn internal search (requires login)
linkedin_url = "https://www.linkedin.com/search/results/people/?keywords=" + urllib.parse.quote(query)

print("LinkedIn search:", linkedin_url)
webbrowser.open(linkedin_url)

#%% Google search for a person on LinkedIn

google_url = "https://www.google.com/search?q=" + urllib.parse.quote(f"site:linkedin.com/in {query}")

print("Google search:", google_url)
webbrowser.open(google_url)

#%%
