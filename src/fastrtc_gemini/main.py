from fastrtc import Stream, ReplyOnPause
import numpy as np


def echo(audio: tuple[int, np.ndarray]):
    # The function will be passed the audio until the user pauses
    # Implement any iterator that yields audio
    # See "LLM Voice Chat" for a more complete example
    yield audio


stream = Stream(
    handler=ReplyOnPause(echo),
    modality="audio",
    mode="send-receive",
)

stream.ui.launch()


# def main() -> None:
#     print("Hello from fastrtc-gemini!")
#     app, str1, str2 = stream.ui.launch()
#     print("app", app)
#     print("str1", str1)
#     print("str2", str2)
