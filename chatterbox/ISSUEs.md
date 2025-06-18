# watermarker NPE

    /home/justin/work/explore/play-python/chatterbox/.venv/lib/python3.11/site-packages/diffusers/models/lora.py:393: FutureWarning: `LoRACompatibleLinear` is deprecated and will be removed in version 1.0.0. Use of `LoRACompatibleLinear` is deprecated. Please switch to PEFT backend by installing PEFT: `pip install peft`.
      deprecate("LoRACompatibleLinear", "1.0.0", deprecation_message)
    Traceback (most recent call last):
      File "/home/justin/work/explore/play-python/chatterbox/generate.py", line 22, in <module>
        main()
      File "/home/justin/work/explore/play-python/chatterbox/generate.py", line 6, in main
        model = ChatterboxTTS.from_pretrained(device="cuda")
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/justin/work/explore/play-python/chatterbox/.venv/lib/python3.11/site-packages/chatterbox/tts.py", line 180, in from_pretrained
        return cls.from_local(Path(local_path).parent, device)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/justin/work/explore/play-python/chatterbox/.venv/lib/python3.11/site-packages/chatterbox/tts.py", line 165, in from_local
        return cls(t3, s3gen, ve, tokenizer, device, conds=conds)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/justin/work/explore/play-python/chatterbox/.venv/lib/python3.11/site-packages/chatterbox/tts.py", line 126, in __init__
        self.watermarker = perth.PerthImplicitWatermarker()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    TypeError: 'NoneType' object is not callable

Cause: stale setuptools and pip
Resolution: upgrade setuptools and pip

    uv pip install -U setuptools pip
