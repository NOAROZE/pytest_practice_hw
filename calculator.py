class Calculator:
    def is_positive(self, a: int):
        return a > 0

    def count_vowels(self, text: str):
        count = 0
        for ch in text.lower():
            if ch in "aeiou":
                count += 1
        return count