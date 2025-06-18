import torchaudio as ta
from chatterbox.tts import ChatterboxTTS


def main():
    model = ChatterboxTTS.from_pretrained(device="cuda")

    text = """
    Ezreal and Jinx teamed up with Ahri, Yasuo, and Teemo
    to take down the enemy's Nexus in an epic late-game pentakill.
    """
    wav = model.generate(text)
    ta.save("test-1.wav", wav, model.sr)

# If you want to synthesize with a different voice, specify the audio prompt
    AUDIO_PROMPT_PATH = "YOUR_FILE.wav"
    wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
    ta.save("test-2.wav", wav, model.sr)


if __name__ == "__main__":
    main()

