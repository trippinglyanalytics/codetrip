# CompTIA Data Systems Trivia Game

A terminal-based, menu-driven Python quiz game for CompTIA Data Systems certification preparation.

## Features

### Game Modes
- **Study Mode**: Answer questions with immediate feedback and explanations
- **Exam Mode**: Take a graded quiz with results shown at the end

### Functionality
- ✅ Topic selection (filter questions by specific topics)
- ✅ Customizable number of questions (1-35)
- ✅ Score tracking and performance metrics
- ✅ Topic-based performance breakdown
- ✅ Review missed questions with explanations
- ✅ Clean menu-driven interface
- ✅ 35 curated questions covering all CompTIA Data Systems topics

## Topics Covered

1. **Backup & Recovery** - Backup strategies and recovery procedures
2. **Data Systems** - Data warehouses, data lakes, and data marts
3. **Database Design** - Normalization, keys, relationships, and data models
4. **Database Fundamentals** - Relational, NoSQL, graph, and column-oriented databases
5. **Deployment** - Cloud architectures (IaaS, PaaS, SaaS)
6. **Performance** - Indexing, monitoring, and load balancing
7. **SQL** - Queries, commands, joins, and clauses
8. **Scripting** - PowerShell, Bash, and SQL scripting
9. **Security** - Encryption, SQL injection, least privilege, and data masking
10. **Transactions** - ACID principles and transaction management

## Installation

No installation required! Just Python 3.6+ is needed.

```bash
cd datasys_trivia
python3 main.py
```

Or make it executable:

```bash
chmod +x main.py
./main.py
```

## Usage

### Quick Start

1. Run the game:
   ```bash
   python3 main.py
   ```

2. Enter your name

3. Choose a mode:
   - **Study Mode** - See explanations immediately after each answer
   - **Exam Mode** - Get graded at the end

4. Select topics (or choose "all")

5. Choose number of questions

6. Answer and learn!

### Example Session

```
==============================================================
  CompTIA Data Systems Trivia
==============================================================

Welcome to the CompTIA Data Systems certification prep game!

This game helps you prepare for the CompTIA Data Systems exam.
You can study with instant feedback or take practice exams.

Enter your name: Alice

Welcome, Alice! Let's get started.

Press ENTER to continue...
```

## File Structure

```
datasys_trivia/
│
├── main.py              # Main game logic and UI
├── question_bank.py     # All questions and topic helpers
├── utils.py             # Utility functions for display
└── README.md            # This file
```

## Question Bank

The game includes **35 questions** covering:
- Easy, Medium difficulty levels
- All major CompTIA Data Systems topics
- Detailed explanations for each answer

Topics are automatically generated from the question bank, ensuring consistency.

## Code Structure

### main.py
- `main()` - Entry point and game loop
- `main_menu()` - Display and handle menu choices
- `choose_topics()` - Topic selection interface
- `get_number_of_questions()` - Question count selection
- `run_round()` - Execute a quiz round (study or exam mode)
- `ask_question()` - Display and handle individual questions
- `show_summary()` - Display final results and performance metrics
- `review_missed_questions()` - Review mode for incorrect answers

### question_bank.py
- `QUESTION_BANK` - List of all 35 questions
- `TOPICS` - Dynamically generated from questions
- `DIFFICULTIES` - Dynamically generated difficulty levels
- `get_questions_by_topic()` - Filter helper
- `get_questions_by_difficulty()` - Filter helper

### utils.py
- Terminal display utilities
- Input validation helpers
- Screen management functions

## Future Enhancements (Version 2)

Potential features for future versions:
- Save/load progress
- Leaderboard system
- Timed exam mode
- Question difficulty selection
- Study statistics tracking
- Export results to file
- Add more questions (target: 50-100)

## Requirements

- Python 3.6 or higher
- Terminal/command prompt
- No external dependencies

## License

Educational project for CompTIA Data Systems certification preparation.

## Author

Created as a portfolio project demonstrating:
- Python programming
- Menu-driven terminal applications
- Data structure management
- User experience design
- Educational software development
