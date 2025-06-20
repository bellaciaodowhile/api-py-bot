from flask import Flask, jsonify, request
import pyautogui
import shutil
import base64
import time
import os
import pyperclip 

app = Flask(__name__)


@app.route('/send_message', methods=['POST'])  # Change to POST method
def send_message():
    try:
        # Get the message from the request body
        data = request.get_json()
        message = data.get('message', '/start')  # Default to '/start' if no message is provided

        # Step 1: Open Telegram
        os.startfile("C:\\Users\\User\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")  # Adjust the path as needed
        time.sleep(0.3)  # Wait for Telegram to open
        
        # Step 2: Navigate to the chat group
        pyautogui.moveTo(407, 175)  # Coordinates for Test-id-chat
        pyautogui.click()
        
        # Step 3: Click on the input field
        time.sleep(0.5)
        pyautogui.moveTo(626, 667)  # Coordinates for the input field
        pyautogui.click()
        
        # Step 4: Type and send the message
        pyautogui.typewrite(message)
        time.sleep(0.5)
        pyautogui.press('enter')

        pyautogui.moveTo(632, 426)
        time.sleep(1)
        pyautogui.rightClick()
        pyautogui.moveTo(699, 514)  # Coordinates for the copy option
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        # Step 10: Get the copied text from the clipboard
        copied_text = pyperclip.paste() 

        return jsonify({"status": "success", "message": "Message sent successfully.", "response": copied_text}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500



@app.route('/send_file', methods=['POST'])
def send_file():
    try:
        # Get the message and file path from the request body
        data = request.get_json()
        message = data.get('message', '/5stats all')  # Default to '/start' if no message is provided
        file_path = data.get('file_path')  # Get the file path from the request

        # Step 2: Open Telegram
        os.startfile("C:\\Users\\User\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")  # Adjust the path as needed
        time.sleep(0.5)  # Wait for Telegram to open

        # Step 3: Navigate to the chat group
        pyautogui.moveTo(407, 175)  # Coordinates for Falleris Bot
        pyautogui.click()

        # Step 4: Click on the input field
        time.sleep(0.5)
        pyautogui.moveTo(626, 667)  # Coordinates for the input field
        pyautogui.click()

        # Step 5: Type and send the message
        pyautogui.typewrite(message)
        time.sleep(0.5)
        pyautogui.press('enter')

        # Step 6: Copy the file path
        pyautogui.moveTo(691, 598)  # Location of the file
        time.sleep(2)
        pyautogui.rightClick()
        pyautogui.moveTo(782, 469)  # Coordinates for the copy option
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(691, 598)  # Location of the file
        time.sleep(0.5)
        pyautogui.rightClick()
        time.sleep(0.5)
        pyautogui.moveTo(760, 426)  # Save file
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.press('enter')

        # Step 7: Get the copied text from the clipboard
        copied_text = pyperclip.paste()
    
        return jsonify({
            "status": "success",
            "message": "Message sent successfully.",
            "filename": copied_text  # Include the base64 encoded file
        }), 200

        return jsonify({"status": "success", "message": "Message sent successfully, but no file was copied."}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/get_mouse_position', methods=['GET'])
def get_mouse_position():
    try:
        # Allow a few seconds to switch to the desired screen
        print("You have 5 seconds to move your mouse to the desired position...")
        time.sleep(5)  # Wait for a moment
        # Get the current mouse position
        x, y = pyautogui.position()
        print(f"Current mouse position: ({x}, {y})")
        return jsonify({"x": x, "y": y}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)


# # Allow a few seconds to switch to the desired screen
# print("You have 5 seconds to move your mouse to the desired position...")
# time.sleep(5)

# # Get the current mouse position
# x, y = pyautogui.position()
# print(f"Current mouse position: ({x}, {y})")
