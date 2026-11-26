import os

WORD = "doomscrolling"

# The entry must be exactly one word of 1-30 characters.
assert 1 <= len(WORD) <= 30, f"word is {len(WORD)} chars"
assert " " not in WORD and "\n" not in WORD
assert WORD.isalpha(), "a single word holds letters only"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(WORD)
