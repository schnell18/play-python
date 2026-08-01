import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from chatterbox.tts import ChatterboxTTS

# device = "cuda"  # or "cpu" / "mps"
device = "cpu"


def english(template, output):
    text = """
        Ezreal and Jinx teamed up with Ahri, Yasuo, and
        Teemo to take down the enemy's Nexus in an epic late-game pentakill.
    """
    model = ChatterboxTTS.from_pretrained(device=device)
    wav = model.generate(text, audio_prompt_path=template)
    ta.save(output, wav, model.sr)


def french(template, output):
    french_text = """
        Bonjour, comment ça va? Ceci est le modèle de synthèse vocale
        multilingue Chatterbox, il prend en charge 23 langues.
    """
    # Multilingual V3 examples
    # To use the legacy V2 multilingual checkpoint, omit t3_model or pass t3_model="v2".
    model = ChatterboxMultilingualTTS.from_pretrained(device=device, t3_model="v3")
    wav_french = model.generate(
        french_text, language_id="fr", audio_prompt_path=template
    )
    ta.save(output, wav_french, model.sr)


def chinese(template, output):
    chinese_text = "你好，今天天气真不错，希望你有一个愉快的周末。"
    # Multilingual V3 examples
    model = ChatterboxMultilingualTTS.from_pretrained(device=device, t3_model="v3")
    wav_chinese = model.generate(
        chinese_text, language_id="zh", audio_prompt_path=template
    )
    ta.save(output, wav_chinese, model.sr)


def main():
    # If you want to synthesize with a different voice, specify the audio prompt
    audio_prompt_path = "/home/justin/justin.wav"
    english(audio_prompt_path, "test-english.wav")
    french(audio_prompt_path, "test-french.wav")
    chinese(audio_prompt_path, "test-chinese.wav")


if __name__ == "__main__":
    main()
