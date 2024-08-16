import time
from gtts import gTTS
import os

class TodoList:
    @staticmethod
    def user_input():
        i = 1
        Activities = []

        while True:
            user_input = input("Enter your activity (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            
            # Ask the user if they want to use the current time or input their own
            use_current_time = input("Do you want to use the current time? (y/n): ").lower()
            if use_current_time == 'y':
                current_time = time.strftime('%I:%M:%S')
            else:
                # Allow user to enter time in HH:MM:SS format
                while True:
                    current_time = input("Enter the time for this activity (HH:MM:SS): ")
                    try:
                        time.strptime(current_time, '%I:%M:%S')
                        break
                    except ValueError:
                        print("Invalid time format. Please enter time as HH:MM:SS.")

            # Add the activity and the timestamp to the list as a tuple
            Activities.append((user_input, current_time))
            print(f"{i}: {user_input}                  {current_time}")
            i += 1

        # Print the stored activities
        for idx, (activity, timestamp) in enumerate(Activities, start=1):
            print(f"{idx} Activity: {activity} at {timestamp}")

        while True:
            now = time.strftime('%I:%M:%S')
            for activity, activity_time in Activities:
                if now == activity_time:
                    # Convert the text to speech
                    text = f"It's time for your {activity}"
                    tts = gTTS(text=text, lang='en', slow=False)
                    tts.save("reminder.mp3")
                    # Play the converted speech using the default media player
                    os.system("start reminder.mp3")  # Windows
                    time.sleep(1)  # Prevent repeated triggers within the same second


if __name__ == "__main__":
    TodoList.user_input()



