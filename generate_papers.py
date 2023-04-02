#%%
import openai
import os
#%%
# Set up API key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
#%%
# Function to generate text
def generate_text(prompt, model="text-davinci-003", temperature=0.7, max_tokens=100):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response

# Make a test query
prompt = "List the top 10 drone mapping variables."
response = generate_text(prompt)

# Get the generated text
response_text = response.choices[0].text.strip()

# Get the tokens used
tokens_used = response.usage["total_tokens"]

print("Generated text:")
print(response_text)
print("\nTokens used:", tokens_used)

# %%
