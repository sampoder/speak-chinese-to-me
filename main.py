from playsound import playsound
from gtts import gTTS
import random
import os

questions = ['你觉得现在最大的环境问题是什么？', '你觉得对你日常造成最大影响的环境问题是什么', '你觉得在学校内我们能做什么？', '你觉得在社区里我们能做什么？', '你觉得我们在家里能做什么？', '你觉得新加坡的环境保护怎么样？', '你会成为绿色的一代吗？']

random.shuffle(questions)

for i in range(len(questions) - 1):
    tts = gTTS(questions[i], lang='zh-CN')
    tts.save('tmp.mp3')
    playsound('tmp.mp3')
    input('Press Enter to continue...')

os.remove('tmp.mp3')