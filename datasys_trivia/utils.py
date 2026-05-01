"""
Utility functions for CompTIA Data Systems Trivia game.
"""


def clear_screen():
    """Clear the terminal screen."""
    print("\033[H\033[J", end="")


def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def print_separator():
    """Print a visual separator."""
    print("-" * 60)


def get_input(prompt, valid_options=None):
    """Get user input with validation."""
    while True:
        user_input = input(prompt).strip().upper()
        if valid_options is None:
            return user_input
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")


def confirm_action(prompt="Are you sure? (Y/N): "):
    """Get yes/no confirmation from user."""
    response = get_input(prompt, ["Y", "N"])
    return response == "Y"


def wait_for_enter(message="Press ENTER to continue..."):
    """Wait for user to press enter."""
    input(message)
