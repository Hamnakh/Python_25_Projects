import time

def countdown_timer():
    try:
        # Get input from user in seconds
        seconds = int(input("Enter time in seconds: "))
        
        while seconds > 0:
            # Convert to minutes and seconds format
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            
            # Display timer in MM:SS format
            timer_display = f'{minutes:02d}:{remaining_seconds:02d}'
            print(timer_display, end='\r')  # \r helps to update in the same line
            
            # Wait for 1 second
            time.sleep(1)
            seconds -= 1
        
        print("\nTime's up!")
        
    except ValueError:
        print("Please enter a valid number of seconds!")
    except KeyboardInterrupt:
        print("\nTimer stopped by user!")

if __name__ == "__main__":
    print("Welcome to Countdown Timer!")
    countdown_timer()
