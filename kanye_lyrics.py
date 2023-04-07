import markovify

# Load the Kanye West lyrics text file
with open("kanye_lyrics.txt") as f:
    text = f.read()

# Build the Markov model
model = markovify.Text(text)

# Generate a new Kanye West quote
quote = model.make_sentence()

print(quote)
