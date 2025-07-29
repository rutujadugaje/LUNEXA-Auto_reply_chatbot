import pyautogui
import pyperclip
import time

import google.generativeai as genai
# from gemini import auto_reply_gemini_model


if __name__ == "__main__":
    # Step 1: Click on chrome icon at coordinateds(962, 1053)
    pyautogui.click(962, 1053)
    time.sleep(1)  # wait for the window to open

    while True:
    
        pyautogui.moveTo(621, 189)
        pyautogui.dragTo(1888, 946, duration=3, button='left') #drag for 1 second
        time.sleep(2)

        pyautogui.hotkey('ctrl', 'c')

        pyautogui.click(1879, 527)
        time.sleep(1)  # wait for clipboard to update

        copied_text = pyperclip.paste()
        print("Copied Text:\n", copied_text)

        # def auto_reply_gemini_model():
        #     model = genai.GenerativeModel('gemini-1.5-flash')
        #     response = model.generate_content(' You are a person named harry who speaks hindi as well as english. He if from India and is a coder. You analyze that history and respond like harry')
        #     print(response.text)
