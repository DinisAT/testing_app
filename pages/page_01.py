from main.main import printing
import streamlit as st

st.title("Page 01")

st.write(printing())


import requests

url = "https://api.d-id.com/talks"

payload = {
    "script": {
        "type": "text",
        "subtitles": "false",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JasonNeural",
            "voice_config": { "style": "Hopeful" }
        },
        "input": "Feeling anxious how have you been doing?"
    },
    "config": {
        "fluent": "false",
        "pad_audio": "0.0",
        "driver_expressions": { "expressions": [
                {
                    "expression": "happy",
                    "start_frame": 0,
                    "intensity": 1
                }
            ] },
        "stitch": True
    },
    "source_url": "https://clips-presenters.d-id.com/william/FPvBkeR0kv/bAIOAUOG33/image.png"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic WkdsdWFYTmhiV0ZrYjNKQVoyMWhhV3d1WTI5dDpEYUhKZmdVakpLcFlQWTdQd0QwQkc="
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
