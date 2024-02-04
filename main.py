import dotenv, os
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import threading  
from datetime import datetime

dotenv.load_dotenv()
client = WebClient(token=os.getenv("SLACKBOT_TOKEN"))
app = Flask(__name__) 

def upload_file_to_slack(channel_id, file_path, title, callback):
    try:
        response = client.files_upload_v2(
            channels=channel_id,
            file=file_path,
            title=title,
        )
        response_message = {
            "response_type": "in_channel",
            "text": f"Meeting note file uploaded successfully.",
        }
        print(f"File '{response['file']['title']}({response['file']['name']})' uploaded successfully: {datetime.fromtimestamp(float(response['file']['created'])).strftime('%Y-%m-%d %H:%M:%S')}")
    except SlackApiError as e:
        response_message = {
            "response_type": "in_channel", 
            "text": f"Failed to upload meeting note file : {e.response['error']}",
        }
        print(f"Error uploading file: {e.response['error']}")
    callback(response_message, channel_id) 
    
def handle_upload_finished(response_message, channel_id):
    try:
        response = client.chat_postMessage(
            channel=channel_id,
            text=response_message["text"]
        )
        print(f"Finish message uploaded successfully: {datetime.fromtimestamp(float(response['ts'])).strftime('%Y-%m-%d %H:%M:%S')}")
    except SlackApiError as e:
        assert e.response["error"]
        print(f"Error uploading finish message: {e.response['error']}")

@app.route('/slack/command', methods=['POST'])
def handle_command():
    data = request.form
    command = data['command']
    channel_id = data['channel_id']
    notion_url = data['text']
    notion_pageid = notion_url.split("-")[-1].split("?")[0]

    if command == '/meetingnote': 
        thread = threading.Thread(target=upload_file_to_slack, args=(
            channel_id,
            "GSA_report_template.hwp",
            "Meeting Note File",
            handle_upload_finished
        ))
        thread.start()
        return jsonify({
            "response_type": "in_channel",
            "text": "Generating meeting note file...",
        })

if __name__ == '__main__':
    app.run(debug=True)