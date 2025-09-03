import os

from fastrtc import ReplyOnPause, Stream, get_stt_model, get_tts_model
from openai import OpenAI
import numpy as np

google_gemini_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
stt_model = get_stt_model()
tts_model = get_tts_model()


def echo(audio: tuple[int, np.ndarray]):
    # The function will be passed the audio until the user pauses
    # Implement any iterator that yields audio
    # See "LLM Voice Chat" for a more complete example
    prompt = stt_model.stt(audio)
    if not prompt:
        print("prompt is empty")
        prompt = "Can you repeat that?"
    else:
        print(f"prompt: {prompt}")

    response = google_gemini_client.chat.completions.create(
        # model="gemini-2.0-flash",
        model="gemini-1.5-flash",
        messages=[
            {
                "role": "system",
                "content": "You are an interactive kids bedtime storytelling Voice AI assistant named Hannah. Use simple language with a range of vocabulary. Do not use emojis or any kind of formatting.",
            },
            {"role": "user", "content": prompt},
        ],
        modalities=["text"],
        max_tokens=200,
        temperature=1,
        top_p=0.95,
    )

    response_message_content = response.choices[0].message.content
    if response_message_content is None:
        print("response_message_content is empty")
        print(f"response: {response}")
        response_message_content = ""
    for audio_chunk in tts_model.stream_tts_sync(response_message_content):
        yield audio_chunk


stream = Stream(
    handler=ReplyOnPause(echo),
    modality="audio",
    mode="send-receive",
)

stream.ui.launch()
