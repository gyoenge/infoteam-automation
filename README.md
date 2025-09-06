# Infoteam Meeting Minutes Automation Project 

- GIST Student Council Information Bureau (INFOTEAM) Project
- Developing a Meeting Minutes Automation Service
- This service converts team meeting minutes in Notion to HWP files and delivers them via a Slackbot
- Python Project

### Preview

(example of meeting minutes template)

<p align="center">
<img src="https://github.com/user-attachments/assets/22b82ae9-0165-4637-8132-e41234839d02" alt="automation_mockup" width="80%" />
</p>

---

## **Description**

### **1. .env File Configuration**

Create a `.env` file in the root directory with the following variables:

```
NOTION_TOKEN={Auth token for your Notion workspace}
SLACKBOT_TOKEN={Auth token for the 'Auto Meeting Note' Slack bot}
```

1.  **NOTION\_TOKEN:** Contact the Infoteam lead for this token.
2.  **SLACKBOT\_TOKEN:** Contact the team lead for this token (or find it on your Slack bot's configuration page).

### **2. How to Run**

1.  **Create a Conda virtual environment.**

    ```bash
    conda create -f environment.yaml
    conda activate automation
    ```

    *(Note: Assuming `automation.yaml` is the intended filename, renamed to a more standard `environment.yaml` for clarity. If the file is indeed named `automation.yaml`, please keep that name.)*

2.  **Run the main script.** (Ensure your execution environment is set to the correct Conda environment.)

    ```bash
    python main.py
    ```

3.  **Start an ngrok tunnel to your local server.** (Pay attention to your authtoken and port number.)

    ```bash
    ngrok authtoken <YOUR_AUTH_TOKEN>
    ngrok http 5000
    ```

4.  **Copy the https URL** from the "Forwarding" line in your ngrok dashboard.

5.  **Update the Slack command URL.** Go to your Slack app's slash command configuration page. In the settings for the `/meetingnote` command, paste the URL you copied in step 4 into the "Request URL" field. Then, append `/slack/command` to the end of the URL. (Contact the team lead if you need help.)
    *Example: `https://your-ngrok-url.ngrok.io/slack/command`*

### **3. How to Use the Slack Slash Command**

1.  Go to the **`#meeting_notes`** channel within the Infoteam Slack workspace.

2.  Type the following command in the chat: `/meetingnote [notion page url]`

      * Replace `[notion page url]` with the copied link to your Notion meeting minutes page. \<br/\>
      * Location of the Notion meeting minutes page link: \<br/\>

3.  The Slack bot will generate the meeting minutes and upload the file to the channel as shown below.


