import random
import re
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.chain = defaultdict(list)
        self.starts = []

    def add_text(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        if len(words) < 2:
            return
        self.starts.append(words[0])
        for i in range(len(words) - 1):
            self.chain[words[i]].append(words[i + 1])

    def generate_text(self, total_words=50, words_per_line=7):
        if not self.starts:
            return "No text was provided to build the chain."

        current_word = random.choice(self.starts)
        result = [current_word]
        
        for _ in range(total_words - 1):
            next_words = self.chain.get(current_word)
            if not next_words:
                break
            current_word = random.choice(next_words)
            result.append(current_word)

        # Format result into poem-style lines
        lines = []
        for i in range(0, len(result), words_per_line):
            line = ' '.join(result[i:i+words_per_line])
            lines.append(line)

        return '\n'.join(lines)

def main():
    input_file = input("📄 Enter the path to your .txt file (e.g. poem.txt): ")

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("❌ File not found. Please check the path and try again.")
        return

    chain = MarkovChain()
    chain.add_text(text)

    generated_text = chain.generate_text(total_words=60, words_per_line=7)

    output_file = "generated_output.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(generated_text)

    print(f"✅ Generated poem saved in: {output_file}")

if __name__ == "__main__":
    main()
