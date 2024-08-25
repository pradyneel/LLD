# Interface Segregation Principle

# Audio Player Interface
class AudioPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError
    
    def stop_audio(self):
        raise NotImplementedError
    
    def adjust_audio_volume(self, volume):
        raise NotImplementedError

# Video Player Interface
class VideoPlayer:
    def play_video(self, video_file):
        raise NotImplementedError
    
    def stop_video(self):
        raise NotImplementedError
    
    def adjust_video_brightness(self, brightness):
        raise NotImplementedError

# MP3 Player
class MP3Player(AudioPlayer):
    def play_audio(self, audio_file):
        # Play MP3 file
        pass
    
    def stop_audio(self):
        # Stop audio playback
        pass
    
    def adjust_audio_volume(self):
        # Adjust Volume
        pass

# Video Player
class AviVideoPlayer(VideoPlayer):
    def play_video(self, video_file):
        # Play AVI video file
        pass

    def stop_video(self):
        # Stop video playback
        pass

    def adjust_video_brightness(self, brightness):
        # Adjust video brightness
        pass

# Implementing with both interfaces
class MultiMediaPlayer(AudioPlayer, VideoPlayer):
    # Implements methods from oht AudioPlayer and VideoPalyer interfaces
    pass