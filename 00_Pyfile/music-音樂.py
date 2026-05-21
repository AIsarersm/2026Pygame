import pygame
import time
pygame.init()
pygame.mixer.init()

# mixer主要用於聲效播放(時長短)，它會先加載到內存中，然後去調用
# 與mixer不同的是，music是用stream(流)的方式去加載，即「邊播邊加載」，因此適合用於長時長的音樂播放(一般用於背景音樂上)

# 1. 加載音樂
# load(filename) -> None
music_file_path_mp3 = "./resources/mucis/file_example_MP3_700KB.mp3"
music_file_path_ogg = "./resources/mucis/file_example_OOG_1MG.ogg"
music_file_path_wav = "./resources/mucis/file_example_WAV_1MG.wav"
music_file_path = music_file_path_mp3

pygame.mixer.music.load(music_file_path)
print("Step1. 加載音樂")

# 2. 播放音樂, play(loops=0, start=0.0, fade_ms=0) -> None
# loops 為repeat times，-1為無限循環
# start為開始的seconds
# fade_ms 為多毫秒後，音樂會自動升到最大聲
pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)  # 同樣為非阻塞式
print("Step2. 播放音樂")
time.sleep(2)

# 3. 設置音量大小，set_volume(volume) -> None，0<=volume<=1
pygame.mixer.music.set_volume(0.5)
# 4. 獲取音量大小
print(f"現時音量大小是{pygame.mixer.music.get_volume()}")
time.sleep(5)

# 5. 重新播放音樂，rewind() -> None
# pygame.mixer.music.rewind()
# print("Step3. 重播音樂")
# time.sleep(2)

# 6. 音樂暫停，pause() -> None
pygame.mixer.music.pause()
print("Step4. 暫停音樂")
time.sleep(2)

# 7. 音樂恢复，
pygame.mixer.music.unpause()
print("Step5. 音樂恢复")
time.sleep(2)

# 8 音樂停止，stop() -> None
# pygame.mixer.music.stop()
# print("Step6. 音樂停止")


# 9. 若需要加載其他music，需要先unload，再load入新music
# unload() -> None
pygame.mixer.music.unload()  # 常見做法: 先調用stop()再調用
pygame.mixer.music.load(music_file_path_wav)
pygame.mixer.music.play()
print("Step7. 播放新的音樂")
time.sleep(4)

# 10. 若想播完A聲樂後，接著自動播B音樂，可用queue(filename) -> None
music_file2_path = "./resources/mucis/wav_sample2.wav"
pygame.mixer.music.queue(music_file2_path)
print("Step8. 接著播放下一首音樂")
time.sleep(10)

pygame.quit()
