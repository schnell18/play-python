import torchaudio as ta
from chatterbox.tts import ChatterboxTTS


def main():
    model = ChatterboxTTS.from_pretrained(device="cuda")

    text = """Large Language Models have exhibited remarkable capabilities in
tasks such as natural language comprehension, content generation, and knowledge
retrieval. However, training and serving these models require substantial
computational resources, posing a significant barrier to AI application
development and research. To address these challenges, various model
compression techniques have been explored, with quantization emerging as a key
approach.
"""

    # Nonetheless, existing quantization methods predominantly apply
    # uniform quantization configurations, failing to account for the varying
    # quantization difficulty across different layers in billion-scale models.
    # """
    # wav = model.generate(text)
    # ta.save("thesis-abstract.wav", wav, model.sr)

    # If you want to synthesize with a different voice, specify the audio prompt
    reference_audio_path = "justin.wav"
    wav = model.generate(
        text,
        exaggeration=0.8,
        cfg_weight=0.3,
        temperature=0.2,
        audio_prompt_path=reference_audio_path,
    )
    ta.save("thesis-abstract-justin.wav", wav, model.sr)


if __name__ == "__main__":
    main()
