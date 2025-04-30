# Markov Chain Text Composer

A Python project that uses Markov chains to analyze text patterns and generate new text based on learned patterns. This project is particularly useful for analyzing and generating song lyrics, poetry, or any other form of text.

## What is a Markov Chain?

A Markov chain is a mathematical system that transitions from one state to another according to certain probabilistic rules. In the context of text generation, it's used to model the probability of words following other words based on patterns in the input text.

## Features

- Analyze text patterns from input text
- Generate new text based on learned patterns
- Simple and intuitive interface
- Customizable text generation length

## Requirements

- Python 3.x
- No external dependencies required (uses built-in Python libraries)

## How to Use

1. Clone or download this repository
2. Open `main.py` in your Python environment
3. Modify the example text in the `main()` function with your own text
4. Run the script using:
   ```bash
   python main.py
   ```

## Example Usage

```python
# Create a new Markov chain
chain = MarkovChain()

# Add your text
lyrics = """
Your text goes here
"""

# Add the text to the chain
chain.add_text(lyrics)

# Generate new text
generated_text = chain.generate_text(length=10)
print("Generated text:", generated_text)
```

## How It Works

1. The program splits input text into words
2. It creates a chain of probabilities showing which words follow other words
3. When generating new text, it:
   - Starts with a random word from the input text
   - Follows the chain of probabilities to generate the next word
   - Continues until it reaches the desired length

## Customization

You can modify the following parameters:
- `length` in `generate_text()`: Controls how many words to generate
- Input text: Replace the example lyrics with any text you want to analyze

## License

This project is open source and available for educational purposes.

## Credits

Inspired by Kylie Ying's tutorial on Markov chains and text generation. 