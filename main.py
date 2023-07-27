from user import User
from tutor import Tutor
from curriculum import Curriculum
from progress_tracker import ProgressTracker

def main():
    # Create a user
    user = User()

    # Authenticate the user
    if not user.authenticate():
        print("Authentication failed.")
        return

    # Create a curriculum
    curriculum = Curriculum()

    # Create a tutor
    tutor = Tutor()

    # Create a progress tracker
    progress_tracker = ProgressTracker()

    # Main loop
    while True:
        # Get user input
        voice_input = user.get_voice_input()

        # Convert voice input to text
        text_input = voice_to_text(voice_input)

        # Generate a response
        response = tutor.generate_response(text_input, curriculum)

        # Speak the response
        tutor.speak(response)

        # Update progress
        progress_tracker.update(response, curriculum)

        # Display progress
        progress_tracker.display()

if __name__ == "__main__":
    main()
