import pygame
import time
pygame.init()

# mixer 模組主要用於播放聲效
# 1. mixer使用前需要初始化
# pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None, allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE) -> None
# 其中參數定義如下:
# ‌frequency‌，音频采样率（单位：Hz），值越高音质越好，但需硬件支持。
# ‌默认值‌：44100（44.1kHz，CD标准）‌。
# ‌典型值‌：22050（低音质）、48000（高音质）。

# size‌，量化位数（音频位深），决定动态范围和精度。
# 默认值‌：-16（表示16位有符号整数）‌。
# ‌可选值‌：-8（8位有符号）、16（无符号16位，部分系统不支持）。

# channels‌，声道数，支持单声道或立体声。
# 默认值‌：2（立体声）‌
# 可选值‌：1（单声道）

# buffer‌，音频缓冲区大小（单位：样本数），影响延迟和稳定性。
# ‌默认值‌：512‌。
# ‌小缓冲区‌（如256）：降低延迟，但可能因计算负载导致卡顿。
# 大缓冲区‌（如1024）：提升稳定性，但增加延迟。

# devicename‌，指定音频输出设备名称（需系统支持）。
# 默认值‌：None（自动选择默认设备）‌

# 一般來說pygame.init()已經會對mixer初始化，但如果用戶想更改初始化參數，則需要自行初始化或在pygame.init()前pre_init()
# 可使用特定的keyword arguments 初始化，如pygame.mixer.init(frequency=12345)
pygame.mixer.init()

# 2. 創建一個sound 對象
# 最常用的方法是指定一個路徑創建對象，Sound(filename) -> Sound
wingAudio = 'resources/sound/wing.wav'
wing_sound_obj = pygame.mixer.Sound(wingAudio)

# 2.1 sound對象可以播放聲效，play(loops=0, maxtime=0, fade_ms=0) -> Channel
# loops-> 代表播放一次後重覆多少次，-1代表不斷重覆，5代表會播6次
# maxtime -> 選擇放多播放多少ms
# fade_ms -> will make the sound start playing at 0 volume and fade up to full volume over the time given. The sample may end before the fade-in is complete.
wing_sound_obj.play(10)  # 非阻塞式
time.sleep(1)

# 2.2 停止聲效播放，stop() -> None
# wind_sound_obj.stop()

# 2.3 設置音量大小，set_volume(value) -> None，0<=value<=1，value<0代表不改變
wing_sound_obj.set_volume(0.2)
time.sleep(4)

# 2.4 獲取音量大小，get_volume() -> value
print(f"此時音量大小是{wing_sound_obj.get_volume()}")


# 不使用mixer時，可以調用quit()則會停止所有音效
# pygame.mixer.quit()->None
pygame.mixer.quit()
