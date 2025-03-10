import yt_dlp

def download_video(url, quality='best'):
    # Opciones para yt-dlp
    ydl_opts = {
        'format': quality,  # Calidad dinámica según el parámetro
        'merge_output_format': 'mp4',  # Formato de salida combinado
        'outtmpl': '%(title)s [%(resolution)s].%(ext)s',  # Nombre con resolución
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        },
        # 'ffmpeg_location': 'C:/path/to/ffmpeg.exe',  # Especifica la ruta a FFmpeg si no está en PATH
        'postprocessors': [{  # Asegura la combinación con FFmpeg
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    try:
        # Descargar el video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)  # Obtener info primero
            print(f"Descargando: {info['title']} [{info.get('resolution', 'unknown')}]")
            ydl.download([url])
        print("Video descargado con éxito.")
    except yt_dlp.DownloadError as e:
        print(f"Error al descargar el video: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def main():
    # URL del video
    url = "https://www.youtube.com/watch?v=k_TW3BcRg7k"
    
    # Opciones de calidad
    # 'best' para mejor calidad disponible
    # 'bestvideo[height<=1080]+bestaudio/best' para máximo 1080p
    # 'bestvideo[height<=2160]+bestaudio/best' para máximo 4K
    quality = 'bestvideo[height<=2160]+bestaudio/best'  # Ejemplo para 4K
    
    download_video(url, quality)

if __name__ == "__main__":
    main()