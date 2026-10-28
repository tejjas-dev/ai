# Practical 07 - Rule-Based AI Chatbot

## Aim
Implement a simple rule-based chatbot using regular expression pattern matching.

## Algorithm Description
- **Rules:** List of (regex_pattern, response_list) tuples.
- **Matching:** User input (lowercased) is checked against each pattern using `re.search()`.
- **Response:** First matching pattern triggers a random choice from its response list.
- **Fallback:** If no pattern matches, returns a default "don't understand" message.
- **Exit:** Loop breaks when user input matches bye/goodbye/see you pattern.

## How to Execute
```bash
cd Practical-07-AI-Chatbot
python3 main.py
```
**Sample conversation (from screenshot):**
```
hello
what is your name
how are you
what is AI
machine learning
thank you
bye
```

## Corrections Made
1. **Missing comma** between first two rule tuples (after the closing `]` of the first tuple's response list).
2. **Unclosed string** in college rule: `...questions.] )` → fixed to `...questions." )`
3. **Regex pattern fix:** Original had `c|+|+` for C++; corrected to `c\+\+` (literal `c++`).
4. **Typos fixed in responses** (kept as close to source intent):
   - `Programmingg` → `Programming`
   - `Jave` → `Java`
   - `Happly` → `Happy`
   - `dont't` → `don't`
   - `requre` → `require`
   - `tYPE` → `Type` (in banner)
5. **Missing comma** in AI rule response list (between two strings).
6. **Structure:** Reconstructed the complete rules list from the PDF (the source was split across pages).

> **Note:** Only syntax/structure fixes were applied. Response text typos from the source were corrected for readability but the pattern logic is preserved.

## Sample Output
See `output.txt` for the exact conversation from the screenshot.

## Known Limitations
- Pattern order matters: first match wins (no priority system).
- No context/memory — each turn is independent.
- Regex patterns are simple word-boundary matches; no NLP or intent classification.
- `random.choice` makes output non-deterministic; screenshot shows one possible run.