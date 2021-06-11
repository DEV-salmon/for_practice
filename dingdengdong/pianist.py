from playsound import playsound
import keyboard as key 

def play(key1,music):
    if key.is_pressed(key1):
        playsound(music)
        print(key1)

while True:
    try:
        play('c','/Users/daeyenhyun/Desktop/programing/dingdengdong/pianofile/sound1.wav')
        play('d','/Users/daeyenhyun/Desktop/programing/dingdengdong/pianofile/sound2.wav')
        play('e','/Users/daeyenhyun/Desktop/programing/dingdengdong/pianofile/sound3.wav')
        play('f','/Users/daeyenhyun/Desktop/programing/dingdengdong/pianofile/sound4.wav')
        play('g','/Users/daeyenhyun/Desktop/programing/dingdengdong/pianofile/sound5.wav')
        play('a','/Users/daeyenhyun/Desktop/programing/dingdengdong/pianofile/sound6.wav')
        play('b','/Users/daeyenhyun/Desktop/programing/dingdengdong/pianofile/sound7.wav')
        play('h','/Users/daeyenhyun/Desktop/programing/dingdengdong/pianofile/sound8.wav')
        if key.is_pressed('6'):
            break
    except:
        pass
    
    

