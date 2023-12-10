# Automating Google Calendar with ChatGPT

**For Chinese version please refer to [here](README_CN.md).**

For those who frequently use Google Calendar, they know that adding calendar events can be a cumbersome process, requiring filling in various fields such as event summary, start and end time, time zone, and more. This poses a significant challenge for long-distance couples trying to synchronize their schedules. Our project aims to address this by integrating a large language model (LLM) to automate the addition of events to Google Calendar.

## How to Use
1. First, you need to have a server and clone this repository to the server-side.
2. The LLM used here is the `gpt-3.5-turbo` model from OpenAI, so you will need to register for an API key from OpenAI and add it to the line `openaiKey = 'your-openai-api-key'` in `prompt_gpt.py`. You can register for an API key [here](https://beta.openai.com/signup).
3. Enable the Google API and create a Google Calendar project, as described [here](https://developers.google.com/calendar/api/quickstart/python?hl=en). You need to follow the steps under "Prerequisites," "Set up your environment," and "Install the Google client library." (Make sure you download the generated OAuth 2.0 client ID into the project folder and rename it into `client_secret_calendar.json`)
4. Install the required dependencies by running `pip install -r requirements.txt`.
5. For debugging purposes, run `python app.py`.
6. For deployment, run `nohup python app.py` to run the backend program in the background.

Finally, enter `http://<your-server-ip-address>:<port-number>` in your web browser, replacing the URL with the IP address and port number of your server, to access the application's web page. The IP address and port information are usually displayed when running `app.py`. From there, you can simply enter the event description you want AI to help add in the input box.

## Note
1. The program will redirect to a web page and prompt you to log in to your corresponding Google account on the first run. This operation only occurs once.
2. This web page is compatible with both PC and mobile devices.
3. This project does not provide server-side encryption. Users can add it themselves.