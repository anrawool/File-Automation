# File for experimentation
import __meta
from Middleware import path_manager
from pytube import YouTube
from settings import get_shell_input, ROOT_DIR
from sys import argv
import __meta

url, mode, save_path = get_shell_input(1, argv, exceptions=["-v", None])


class YoutubeDownloader:
    def __init__(self, url, mode, save_path):
        self.mode = mode
        self.video_url = url
        self.save_path = save_path
        if ROOT_DIR not in self.save_path:
            self.save_path = ROOT_DIR + "/" + self.save_path
        try:
            self.yt = YouTube(self.video_url)
        except Exception:
            raise Exception("This link does not exist on YouTube")
        try:
            if self.mode == "-v":
                stream = self.download_video()
            elif self.mode == "-m":
                stream = self.download_video(audio=False)
            elif self.mode == "-a":
                stream = self.download_audio()
            else:
                raise Exception("Mode not available")
        except Exception as e:
            print(e)
            raise Exception("The inputs given are invalid")
        stream.download(output_path=self.save_path, filename=f"{self.yt.title}.mp3")

    def download_video(self, audio=True):
        if audio:
            stream = self.yt.streams.get_highest_resolution()
        else:
            stream = self.yt.streams.filter(only_video=True).first()
        return stream

    def download_audio(self):
        audio_stream = self.yt.streams.filter(only_audio=True).first()
        return audio_stream


if __name__ == "__main__":
    if save_path == None and mode == "-v":
        save_path = f"{path_manager.HOME_DIRECTORY}downloads/videos"
    elif save_path == None and mode == "-a":
        save_path = f"{path_manager.HOME_DIRECTORY}downloads/audio"
    elif save_path == None and mode == "-m":
        save_path = f"{path_manager.HOME_DIRECTORY}downloads/videos/only_video"
    else:
        save_path = f"{path_manager.HOME_DIRECTORY}downloads/videos"
    downloader = YoutubeDownloader(url, mode, save_path)
