import unittest
import golomb
import elias_gamma
import fibonacci
import huffman

phrases_ascii_only = [
        "The quick brown fox jumps over the lazy dog.",
        "Hello, world!",
        "Python is awesome.",
        "Keep calm and code in Python.",
        "Simple is better than complex.",
        "Errors should never pass silently.",
        "Readability counts.",
        "In the face of ambiguity, refuse the temptation to guess.",
        "There should be one-- and preferably only one --obvious way to do it.",
        "Now is better than never.",
        "Code is like humor. When you have to explain it, its bad.",
        "First, solve the problem. Then, write the code.",
        "Any fool can write code that a computer can understand.",
        "Good programmers write code that humans can understand.",
        "Simplicity is the soul of efficiency.",
        "Before software can be reusable it first has to be usable.",
        "Make it work, make it right, make it fast.",
        "Testing leads to failure, and failure leads to understanding.",
        "The only way to learn a new programming language is by writing programs in it.",
        "Talk is cheap. Show me the code.",
        "Walking on water and developing software from a specification are easy if both are frozen.",
        "It always takes longer than you expect.",
        "Adding manpower to a late software project makes it later.",
        "If debugging is the process of removing bugs, then programming must be the process of putting them in.",
        "If the code works, don't touch it.",
        "Software undergoes beta testing shortly before it's released. Beta is Latin for 'still doesn't work.'",
        "There are only two kinds of programming languages: those people always complain about and those nobody uses.",
        "The best thing about a boolean is even if you are wrong, you are only off by a bit.",
        "Documentation is like sex: when it is good, it is very good; when it is bad, it is better than nothing.",
        "Programming isn't about what you know; its about what you can figure out.",
        "Programmers are tools for converting caffeine into code.",
        "Deleted code is debugged code.",
        "Programming is thinking, not typing.",
        "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Mondays code.",
        "Computers are fast; programmers keep it slow.",
        "Code never lies, comments sometimes do.",
        "If you want to go fast, go alone. If you want to go far, go together.",
        "Weeks of coding can save you hours of planning.",
        "Software is like entropy: It is difficult to grasp, weighs nothing, and obeys the Second Law of Thermodynamics.",
        "One mans crappy software is another mans full-time job.",
        "Software and cathedrals are much the same first we build them, then we pray.",
        "The best code is no code at all.",
        "A good programmer looks both ways before crossing a one-way street.",
        "Fast, good, cheap: pick any two.",
        "Programming is not a zero-sum game. Teaching something to a fellow programmer does not take it away from you.",
        "You cant have great software without a great team.",
        "A clean code always looks like it was written by someone who cares.",
        "Your most unhappy customers are your greatest source of learning.",
        "The function of good software is to make the complex appear simple.",
        "Any code of your own that you have not looked at for six or more months might as well have been written by someone else."
]

class TestCodeAlgorithmsMethods(unittest.TestCase):
    def test_golomb(self):
        for phrase in phrases_ascii_only:
            coded_phrase = golomb.code(phrase)
            encoded_phrase = golomb.decode(coded_phrase)
            self.assertEqual(phrase, encoded_phrase)

    def test_elias_gamma(self):
        for phrase in phrases_ascii_only:
            coded_phrase = elias_gamma.code(phrase)
            encoded_phrase = elias_gamma.decode(coded_phrase)
            self.assertEqual(phrase, encoded_phrase)

    def test_fibonacci(self):
        for phrase in phrases_ascii_only:
            coded_phrase = fibonacci.code(phrase)
            encoded_phrase = fibonacci.decode(coded_phrase)
            self.assertEqual(phrase, encoded_phrase)

    def test_huffman(self):
        for phrase in phrases_ascii_only:
            frequencies: [str, int] = count_frequencies(phrase)
            coded_phrase = huffman.code(phrase)
            encoded_phrase = huffman.decode(coded_phrase, frequencies)
            self.assertEqual(phrase, encoded_phrase)

def count_frequencies(phrase: str) -> dict[str, int]:
    frequencies: dict[str, int] = {}
    for char in phrase:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

if __name__ == '__main__':
    unittest.main()