from video import Video
from podcast import Podcast
from video_narrado import VideoNarrado

midias = [
    Video("Aula de Python", 30),
    Podcast("Podcast Tech", 45),
    VideoNarrado("Documentário", 60)
]

for midia in midias:
    midia.mostrar_info()
    midia.reproduzir()
    print("------")
