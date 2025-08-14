import pyautogui
import pyperclip
import time
import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
model = genai.GenerativeModel('gemini-1.5-flash')
client = genai.configure(api_key = os.getenv('GEMINI_API_KEY'))


def is_last_message_from_sender(chat_text: str, sender_name: str = "Vaishnavi") -> bool:
    """
    Checks if the last message in the chat log is from the given sender.
    Works case-insensitively and ignores extra spaces.
    """
    lines = [line.strip() for line in chat_text.strip().splitlines() if line.strip()]

    # Go backwards until we find a message line
    for line in reversed(lines):
        if "]" in line and ":" in line:
            try:
                sender_part = line.split("]", 1)[1].strip()
                sender = sender_part.split(":", 1)[0].strip().lower()
                return sender == sender_name.lower()
            except:
                return False
    return False


def whatsApp():
    print('chat Bot start')
    # Step 1: Click on chrome icon at coordinateds(962, 1053)
    pyautogui.click(962, 1053)
    time.sleep(1)  # wait for the window to open


    while True:
        pyautogui.moveTo(650, 170)
        pyautogui.dragTo(696, 974, duration=3, button='left') #drag for 1 second
        # time.sleep(2)

        pyautogui.hotkey('ctrl', 'c')

        pyautogui.click(702, 987)
        time.sleep(1)  # wait for clipboard to update

        chat_history = pyperclip.paste()
        print("Copied Text:\n", chat_history)


        if is_last_message_from_sender(chat_history, "Vaishnavi"):
        
            prompt = (f"""
                You are not a bot. You reply like a real person — Rutuja Dugaje. Use natural and friendly language. Your job is to respond to target's persong messages as if you're Rutuja herself.

                - Speak naturally in English.
                - You can talk with the sender in also marathi. If the user types in English but the meaning is Marathi, reply in Marathi but type it using English letters (e.g., "Kese ho?" instead of "How are you?").
               
                - Never send translations or explanations.
                - Never make up fake chat messages or assume messages Rutuja never sent.
                - Only respond to the other person’s message — not your own past messages.
                - respond messages in short , Don't give brief responses. Don't ask many question to sender, ask only one question .
                - The sender is female .
                - Be casual, friendly, and real.
                Current chat history:"
                    f"{chat_history}"
                """)

            response = model.generate_content(prompt)
            print(response.text)
            
            pyperclip.copy(response.text)        
            # Step 5: Click on target input box at (702, 987)
            pyautogui.click(702, 987)
            time.sleep(0.5)

            # Step 6: Paste the text using Ctrl+V
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)

            # Step 7: Press Enter
            pyautogui.press('enter')


