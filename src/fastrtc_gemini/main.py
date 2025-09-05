import os
import gradio as gr
from fastrtc import (
    ReplyOnPause,
    WebRTC,
    get_stt_model,
    get_tts_model,
    get_hf_turn_credentials,
)
from openai import OpenAI
import numpy as np

google_gemini_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
stt_model = get_stt_model()
tts_model = get_tts_model()


def response(audio: tuple[int, np.ndarray]):
    # The function will be passed the audio until the user pauses
    # Implement any iterator that yields audio
    # See "LLM Voice Chat" for a more complete example
    prompt = stt_model.stt(audio)
    if not prompt:
        print("prompt is empty")
        prompt = "Can you repeat that?"
    else:
        print(f"prompt: {prompt}")

    response_message_content = ""
    try:
        client_response = google_gemini_client.chat.completions.create(
            # model="gemini-2.0-flash",
            model="gemini-1.5-flash",
            messages=[
                {
                    "role": "system",
                    "content": "You are an interactive kids bedtime storytelling Voice AI assistant named Hannah. Use simple language with a range of vocabulary. No non-vocal sounds are allowed. Do not use emojis or any kind of formatting.",
                },
                {"role": "user", "content": prompt},
            ],
            modalities=["text"],
            max_tokens=200,
            temperature=1,
            top_p=0.95,
        )
        response_message_content = client_response.choices[0].message.content
        if response_message_content is None:
            print(f"response_message_content is empty. response: {client_response}")
            response_message_content = "Sorry, I am still thinking. Can you please try asking me something again?"

    except Exception as e:
        print(f"Error during Gemini API call: {e}")
        response_message_content = "Sorry, something went wrong. Can you please tell me what you would like to hear from me?"

    for audio_chunk in tts_model.stream_tts_sync(response_message_content):
        yield audio_chunk


with gr.Blocks() as stream_ui:
    gr.HTML(
        """
    <h1 style='text-align: center'>
    Hannah The Storyteller (Powered by FastRTC and Gemini)
    </h1>
    """
    )
    with gr.Column():
        with gr.Group():
            audio = WebRTC(
                mode="send-receive",
                modality="audio",
                rtc_configuration=get_hf_turn_credentials,
            )
        audio.stream(
            fn=ReplyOnPause(response), inputs=[audio], outputs=[audio], time_limit=60
        )
    gr.HTML(
        """
        <style>
            button.show-api { display: none !important; }
            a.built-with { display: none !important; }
            button.settings { display: none !important; }
        </style>
        """
    )

stream_ui.launch(
    server_name="0.0.0.0",
    server_port=7860,
    ssr_mode=True,
    strict_cors=False,
)
