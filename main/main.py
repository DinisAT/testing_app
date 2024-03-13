

import streamlit as st
import os
import requests
import json
import time



# list of coach options
coach_dict = { "Peter" : { 'url' : "https://clips-presenters.d-id.com/darren/RYscOXmp8t/CtDjn3POSq/image.png",
                          'voice_id' : "en-US-AndrewNeural",
                            'style' : "Cheerful"},
              "Sean" : {'url' : "https://clips-presenters.d-id.com/william/FPvBkeR0kv/bAIOAUOG33/image.png",
                          'voice_id' : "en-US-JasonNeural",
                            'style' : "Hopeful"},
              "Jenna": {'url' : "https://clips-presenters.d-id.com/amy/sEIU0O2gBy/VrHMAOUSgO/image.png",
                          'voice_id' : "en-US-JennyNeural",
                            'style' : "Hopeful"},
              "Christine": {'url' : "https://clips-presenters.d-id.com/alyssa/Kpjhh2J_rm/Oa9TBDfWdE/image.png",
                          'voice_id' : "en-US-NancyNeural",
                            'style' : "Hopeful"}
}

def createTalk(coach_name, input):
    url = "https://api.d-id.com/talks"

    source_url = coach_dict[coach_name]['url']
    voice_id = coach_dict[coach_name]['voice_id']
    style = coach_dict[coach_name]['style']

    payload = {
        "source_url": source_url,

        "script": {
        "type": "text",
        "subtitles": "false",
        "provider": {
            "type": "microsoft",
            "voice_id": voice_id,
            "voice_config": { "style": style}
        },
        "input": str(input)
    },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0",
            "driver_expressions": {
                    "expressions": [
                        {
                        "expression": "happy",
                        "start_frame": 0,
                        "intensity": 1
                        }]
            },
            "stitch": True
        }

    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic WkdsdWFYTmhiV0ZrYjNKQVoyMWhhV3d1WTI5dDpEYUhKZmdVakpLcFlQWTdQd0QwQkc="
    }

    response = requests.post(url, json=payload, headers=headers)
    #data = json.loads(response.text)
    #id_video = data.get("id")
    return response#id_video #response,

def getTalk(id_video):
    url = "https://api.d-id.com/talks/"+str(id_video)

    headers = {
        "accept": "application/json",
        "authorization": key
    }

    response = requests.get(url, headers=headers)
    return response

def download_video(coach_name, input):
    response, id_video = createTalk(coach_name, input)
    time.sleep(20)
    video_test = getTalk(id_video)
    st.write(f"got the talk ? {video_test}")
    st.write(type(video_test))
    time.sleep(20)
    data = json.loads(video_test.text)
    return data
