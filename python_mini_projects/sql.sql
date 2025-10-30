User Input
   │
   ▼
"3 + 5 * 2"   ← Input string from user
   │
   ▼
Tokenization
   │
   ├─ Split into tokens: ["3", "+", "5", "*", "2"]
   │
   ▼
Parsing / Operator Precedence
   │
   ├─ Identify operations and order:
   │     * Multiplication (*) has higher precedence than addition (+)
   │
   ▼
Evaluation Step 1: Multiplication
   │
   ├─ 5 * 2 = 10
   │
   ▼
Intermediate Result
   │
   ├─ ["3", "+", "10"]
   │
   ▼
Evaluation Step 2: Addition
   │
   ├─ 3 + 10 = 13
   │
   ▼
Final Result
   │
   └─ Display 13 to user
