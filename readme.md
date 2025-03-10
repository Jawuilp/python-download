# Descargador de Videos de YouTube

Script en Python para descargar videos de YouTube en alta calidad con `yt-dlp` y `FFmpeg`.

## Requisitos
- Python 3.6+ ([python.org](https://www.python.org/downloads/))
- FFmpeg: Descarga desde [gyan.dev](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z) y extrae la carpeta `bin`.
- `pip install yt-dlp`

## Instalación
1. Clona o descarga: `git clone https://github.com/[tu-usuario]/[nombre-repositorio].git`
2. Instala: `pip install yt-dlp`
3. Extrae FFmpeg y añade `C:\ruta\a\ffmpeg\bin` al PATH (o usa en `index.py` si no está en PATH).

## Uso
Edita `index.py`:
```python
url = "https://www.youtube.com/watch?v=L9lLSh6WYa8"
quality = 'bestvideo[height<=2160]+bestaudio/best'  # Hasta 4K

## no me hago responsable del uso que se le pueda dar a este script cada persona es responsable del uso que le de
