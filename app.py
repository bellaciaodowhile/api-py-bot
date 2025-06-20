from flask import Flask, jsonify, request
import pyautogui
import time
import os
import pyperclip 

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        message = data.get('message', '/start')
        os.startfile("C:\\Users\\User\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        time.sleep(0.3)
        pyautogui.moveTo(407, 175)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(626, 667)
        pyautogui.click()
        pyautogui.typewrite(message)
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.rightClick()
        pyautogui.moveTo(699, 514)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        copied_text = pyperclip.paste()
        return jsonify({"status": "success", "message": "Message sent successfully.", "response": copied_text}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/send_file', methods=['POST'])
def send_file():
    try:
        data = request.get_json()
        message = data.get('message', '/5stats all')
        file_path = data.get('file_path')
        os.startfile("C:\\Users\\User\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        time.sleep(0.5)
        pyautogui.moveTo(407, 175)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(626, 667)
        pyautogui.click()
        pyautogui.typewrite(message)
        time.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.moveTo(691, 598)
        time.sleep(2)
        pyautogui.rightClick()
        pyautogui.moveTo(782, 469)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(691, 598)
        time.sleep(0.5)
        pyautogui.rightClick()
        time.sleep(0.5)
        pyautogui.moveTo(760, 426)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.press('enter')
        copied_text = pyperclip.paste()
        return jsonify({"status": "success", "message": "Message sent successfully.", "filename": copied_text}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_mouse_position', methods=['GET'])
def get_mouse_position():
    try:
        print("You have 5 seconds to move your mouse to the desired position...")
        time.sleep(5)
        x, y = pyautogui.position()
        print(f"Current mouse position: ({x}, {y})")
        return jsonify({"x": x, "y": y}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)