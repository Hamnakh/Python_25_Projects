import random
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.chain = defaultdict(list)
        self.starts = []

    def add_text(self, text):
        words = text.split()
        if len(words) < 2:
            return

        # Add the first word to starts
        self.starts.append(words[0])

        # Create transitions between words
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            self.chain[current_word].append(next_word)

    def generate_text(self, length=10):
        if not self.starts:
            return "No text has been added to the chain."

        # Start with a random word from starts
        current_word = random.choice(self.starts)
        result = [current_word]

        # Generate the next words
        for _ in range(length - 1):
            if current_word not in self.chain or not self.chain[current_word]:
                break
            current_word = random.choice(self.chain[current_word])
            result.append(current_word)

        return ' '.join(result)

def main():
    # Example usage
    chain = MarkovChain()
    
    # Example lyrics (you can replace these with your own text)
    lyrics = """
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    """
    
    # Add the lyrics to the chain
    chain.add_text(lyrics)
    
    # Generate new text
    generated_text = chain.generate_text(length=10)
    print("Generated text:", generated_text)

if __name__ == "__main__":
    main()
