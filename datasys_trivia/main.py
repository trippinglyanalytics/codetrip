#!/usr/bin/env python3
"""
CompTIA Data Systems Trivia Game
A terminal-based, menu-driven quiz game for CompTIA Data Systems certification preparation.

Features:
- Study Mode: See explanations after each question
- Exam Mode: Graded quiz with final results
- Topic Selection: Filter questions by topic
- Performance Tracking: View topic-based scores
- Review Missed Questions: Learn from mistakes
"""
import random
import sys
from question_bank import QUESTION_BANK, TOPICS, get_questions_by_topic
from utils import (
    clear_screen, print_header, print_separator,
    get_input, confirm_action, wait_for_enter
)


def main():
    """Main entry point for the trivia game."""
    clear_screen()
    print_header("CompTIA Data Systems Trivia")
    print("Welcome to the CompTIA Data Systems certification prep game!")
    print("\nThis game helps you prepare for the CompTIA Data Systems exam.")
    print("You can study with instant feedback or take practice exams.\n")
    
    player_name = input("Enter your name: ").strip()
    if not player_name:
        player_name = "Player"
    
    print(f"\nWelcome, {player_name}! Let's get started.\n")
    wait_for_enter()
    
    # Main game loop
    while True:
        choice = main_menu(player_name)
        
        if choice == "1":
            # Study Mode
            selected_topics = choose_topics(QUESTION_BANK)
            num_questions = get_number_of_questions()
            run_round(QUESTION_BANK, mode="study", selected_topics=selected_topics, 
                     num_questions=num_questions, player_name=player_name)
        
        elif choice == "2":
            # Exam Mode
            selected_topics = choose_topics(QUESTION_BANK)
            num_questions = get_number_of_questions()
            run_round(QUESTION_BANK, mode="exam", selected_topics=selected_topics, 
                     num_questions=num_questions, player_name=player_name)
        
        elif choice == "3":
            # Quit
            clear_screen()
            print_header("Thanks for Playing!")
            print(f"Goodbye, {player_name}! Good luck on your certification exam!\n")
            sys.exit(0)


def main_menu(player_name):
    """Display main menu and get user choice."""
    clear_screen()
    print_header(f"Main Menu - {player_name}")
    print("1. Study Mode (see explanations after each question)")
    print("2. Exam Mode (graded quiz with final results)")
    print("3. Quit")
    print_separator()
    
    choice = get_input("Choose an option (1-3): ", ["1", "2", "3"])
    return choice


def choose_topics(question_bank):
    """Allow user to select topics for the quiz."""
    clear_screen()
    print_header("Topic Selection")
    print("Available topics:")
    print("0. All topics")
    
    for i, topic in enumerate(TOPICS, 1):
        count = len([q for q in question_bank if q["topic"] == topic])
        print(f"{i}. {topic} ({count} questions)")
    
    print_separator()
    print("\nYou can select multiple topics by entering numbers separated by commas")
    print("Example: 1,3,5 or just press ENTER for all topics")
    
    user_input = input("\nEnter your choice(s): ").strip()
    
    if not user_input or user_input == "0":
        print("\nAll topics selected!")
        wait_for_enter()
        return None
    
    try:
        selected_indices = [int(x.strip()) for x in user_input.split(",")]
        selected_topics = [TOPICS[i-1] for i in selected_indices if 1 <= i <= len(TOPICS)]
        
        if selected_topics:
            print(f"\nSelected topics: {', '.join(selected_topics)}")
            wait_for_enter()
            return selected_topics
        else:
            print("\nNo valid topics selected. Using all topics.")
            wait_for_enter()
            return None
    except (ValueError, IndexError):
        print("\nInvalid input. Using all topics.")
        wait_for_enter()
        return None


def get_number_of_questions():
    """Ask user how many questions they want to answer."""
    clear_screen()
    print_header("Number of Questions")
    
    max_questions = len(QUESTION_BANK)
    while True:
        try:
            num = input(f"How many questions would you like to answer? (1-{max_questions}, or press ENTER for 5): ").strip()
            if not num:
                return 5
            num = int(num)
            if 1 <= num <= max_questions:
                return num
            else:
                print(f"Please enter a number between 1 and {max_questions}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def run_round(question_bank, mode="study", selected_topics=None, num_questions=5, player_name="Player"):
    """Run a round of questions in either study or exam mode."""
    clear_screen()
    mode_name = "Study Mode" if mode == "study" else "Exam Mode"
    print_header(f"{mode_name} - {player_name}")
    
    # Filter questions by selected topics
    available_questions = get_questions_by_topic(selected_topics) if selected_topics else question_bank
    
    if not available_questions:
        print("No questions available for selected topics!")
        wait_for_enter()
        return
    
    # Select random questions
    num_questions = min(num_questions, len(available_questions))
    selected_questions = random.sample(available_questions, num_questions)
    
    # Display mode information
    if selected_topics:
        print(f"Topics: {', '.join(selected_topics)}")
    else:
        print("Topics: All")
    
    print(f"Questions: {num_questions}")
    print(f"Mode: {mode_name}")
    print_separator()
    wait_for_enter("\nPress ENTER to begin...")
    
    # Track results
    score = 0
    total = len(selected_questions)
    topic_results = {}  # {topic: {"correct": 0, "total": 0}}
    missed_questions = []
    
    # Ask each question
    for i, question in enumerate(selected_questions, 1):
        result = ask_question(question, mode=mode, question_num=i, total_questions=total)
        
        # Update score
        if result["correct"]:
            score += 1
        
        # Track by topic
        topic = question["topic"]
        if topic not in topic_results:
            topic_results[topic] = {"correct": 0, "total": 0}
        topic_results[topic]["total"] += 1
        if result["correct"]:
            topic_results[topic]["correct"] += 1
        
        # Track missed questions
        if not result["correct"]:
            missed_questions.append({
                "question": question,
                "user_answer": result["user_answer"]
            })
    
    # Show summary
    show_summary(player_name, score, total, topic_results, missed_questions, mode)


def ask_question(question, mode="study", question_num=1, total_questions=1):
    """Ask a single question and return whether it was answered correctly."""
    clear_screen()
    print_header(f"Question {question_num} of {total_questions}")
    
    print(f"Topic: {question['topic']}")
    print(f"Difficulty: {question['difficulty']}")
    print_separator()
    print(f"\n{question['question']}\n")
    
    for option in question["options"]:
        print(option)
    
    print_separator()
    
    # Get user answer
    valid_answers = ["A", "B", "C", "D"]
    user_answer = get_input("\nYour answer (A/B/C/D): ", valid_answers)
    
    # Check if correct
    correct = user_answer == question["answer"]
    
    # In study mode, show immediate feedback
    if mode == "study":
        print()
        if correct:
            print("✓ CORRECT!")
        else:
            print(f"✗ INCORRECT. The correct answer is {question['answer']}.")
        
        print(f"\nExplanation: {question['explanation']}")
        wait_for_enter()
    
    return {
        "correct": correct,
        "user_answer": user_answer
    }


def show_summary(player_name, score, total, topic_results, missed_questions, mode):
    """Display summary of quiz results."""
    clear_screen()
    print_header(f"Quiz Complete - {player_name}")
    
    percentage = (score / total * 100) if total > 0 else 0
    
    print(f"Final Score: {score}/{total} ({percentage:.1f}%)")
    print_separator()
    
    # Performance rating
    if percentage >= 90:
        rating = "Excellent! 🌟"
    elif percentage >= 80:
        rating = "Great job! 👍"
    elif percentage >= 70:
        rating = "Good! Keep studying! 📚"
    elif percentage >= 60:
        rating = "Passing, but room for improvement. 📖"
    else:
        rating = "Keep practicing! 💪"
    
    print(f"Performance: {rating}\n")
    
    # Topic breakdown
    if topic_results:
        print("Performance by Topic:")
        print_separator()
        for topic, results in sorted(topic_results.items()):
            topic_pct = (results["correct"] / results["total"] * 100) if results["total"] > 0 else 0
            print(f"  {topic}: {results['correct']}/{results['total']} ({topic_pct:.1f}%)")
        print()
    
    # Offer to review missed questions
    if missed_questions:
        print(f"\nYou missed {len(missed_questions)} question(s).")
        if confirm_action("Would you like to review them? (Y/N): "):
            review_missed_questions(missed_questions)
    else:
        print("\nPerfect score! You didn't miss any questions! 🎉")
    
    wait_for_enter("\nPress ENTER to return to main menu...")


def review_missed_questions(missed_questions):
    """Allow user to review questions they got wrong."""
    for i, item in enumerate(missed_questions, 1):
        clear_screen()
        print_header(f"Review Missed Question {i}/{len(missed_questions)}")
        
        question = item["question"]
        user_answer = item["user_answer"]
        
        print(f"Topic: {question['topic']}")
        print(f"Difficulty: {question['difficulty']}")
        print_separator()
        print(f"\n{question['question']}\n")
        
        for option in question["options"]:
            print(option)
        
        print_separator()
        print(f"\nYour answer: {user_answer} ✗")
        print(f"Correct answer: {question['answer']} ✓")
        print(f"\nExplanation: {question['explanation']}")
        
        if i < len(missed_questions):
            wait_for_enter("\nPress ENTER for next question...")
        else:
            wait_for_enter("\nPress ENTER to finish review...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
        sys.exit(0)
