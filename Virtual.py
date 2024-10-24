import pyttsx3  # For text-to-speech conversion
import datetime  # To handle date and time
import speech_recognition as sr  # For recognizing speech
import wikipedia  # To fetch summaries from Wikipedia
import webbrowser  # To open web pages in a browser

myName = 'Vhahangwele'  # Name of the assistant

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # Get available voices
engine.setProperty('voice', voices[0].id)  # Set voice (0 is typically the default)

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)  # Pass the audio to the engine
    engine.runAndWait()  # Wait until speaking is finished

def wishme():
    """Greets the user based on the time of day."""
    hour = datetime.datetime.now().hour  # Get current hour
    if hour >= 0 and hour < 12:
        speak('Good morning')  # Morning greeting
    elif hour >= 12 and hour < 18:
        speak('Good afternoon')  # Afternoon greeting
    else:
        speak('Good evening')  # Evening greeting

def hearMe():
    """Listens for a command from the user and returns the recognized text."""
    r = sr.Recognizer()  # Create a Recognizer instance
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print('Listening.....')
        audio = r.listen(source)  # Listen for audio input
        try:
            print('Recognizing......')
            query = r.recognize_google(audio, language='en-US')  # Recognize the speech
            print('You said:', query)  # Output what was recognized
            return query  # Return the recognized text
        except Exception:
            print('Say that again')  # Handle exceptions
            return 'None'  # Return None if recognition fails

if __name__ == "__main__":
    wishme()  # Wish the user when the program starts
    while True:
        query = hearMe().lower()  # Get the user's command and convert to lowercase
        
        # Check for commands
        if 'wikipedia' in query:
            query = query.replace('wikipedia', '')  # Remove 'wikipedia' from the query
            speak('Searching Wikipedia.....')  # Notify user about the search
            result = wikipedia.summary(query.strip(), sentences=2)  # Get a summary from Wikipedia
            speak('According to Wikipedia')  # Speak the context before the result
            speak(result)  # Speak the actual result
        elif 'open google' in query:
            webbrowser.open('www.google.com')  # Open Google in the web browser
        elif 'open ai' in query:
            webbrowser.open('www.openai.com')  # Open OpenAI's website
        elif 'hexSoftware' in query:
            webbrowser.open('https://hexsoftwares.tech/')  # Open HexSoftwares' website
        
        if 'stop' in query:  # Exit the loop if 'stop' is mentioned
            break

                        