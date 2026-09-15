# Pipeline de audio — SIGNS

## Estructura
audio/
├── source/ cancion.mp3 — fuente original
├── stems/ separación Demucs (vocals, bass, drums, other)
├── experiments/ versiones NES/chiptune de prueba
├── archive/ experimentos FFmpeg/bitcrusher descartados
└── tools/ scripts Python del pipeline


## Pipeline objetivo

1. `detect_melody.py` — detección de notas desde vocals.wav
2. `detect_bass.py`   — detección de bajo desde bass_nes.wav
3. `synthesize_chiptune.py` — síntesis NES con ondas cuadrada/triangular/ruido

## Archivos grandes (no versionados)

stems/*.wav y experiments/*.wav están en .gitignore.
Para regenerar los stems: `demucs audio/source/cancion.mp3`

## Asset final del juego

`assets/audio/music/agujetas.ogg`
