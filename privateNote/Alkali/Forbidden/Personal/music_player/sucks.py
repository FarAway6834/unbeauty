#!/usr/bin/python python3

from platform import system as get_platform
from os import system as s
from os import chdir as cd
from os.path import dirname
from os.path import abspath
from time import sleep as sl

cd(dirname(abspath(__file__)))

quit_signal = False
go = 0

def go_prev():
    global go
    go = -1

def go_next():
    global go
    go = 1

def mp3_play_control_tower(k):
    global go
    if go == -1:
        k.prev()
        k.prev()
    go = 0

if get_platform() == "Windows":
    try: from keyboard import add_hotkey as eventListener
    except:
        s('pip install keyboard')
        from keyboard import add_hotkey as eventListener

    def quit_controller():
        global quit_signal
        quit_signal = True

    def ultimite_quit_controll_toggle():
        pass

    eventListener('q', quit_controller)
    eventListener('p', go_prev)
    # eventListener('d', go_next)

    def mp3player_remote_controller():
        pass

else:
    import sys
    import select
    import tty
    import termios

    def check_ispressed_quit_key(sym = 'q'):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd) # nessesurry : store state
        try:
            tty.setcbreak(fd)
            return sys.stdin.read(1) == sym if select.select([sys.stdin], [], [], 0.0)[0] else False
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # nessesurry : load state

    def ultimite_quit_controll_toggle():
        global quit_signal
        if not quit_signal: quit_signal = check_ispressed_quit_key()
    def mp3player_remote_controller():
        if check_ispressed_quit_key(sym = "p"): go_prev()
        #elif check_ispressed_quit_key(sym = ""): go_next()

def for_playlist_comprehention(f):
    with open(f) as fp:
        for k in fp:
            yield k.strip()

class playlists():

    __slots__ = ("__playlist", "__pointer", "__length")

    def __init__(self, playlist):
        self.__playlist = playlist
        self.__length = len(playlist)
        self.__pointer = -1 % self.__length

    def next(self):
        self.__pointer += 1
        self.__pointer %= self.__length
        return self

    def __next__(self):
        return self.next()

    def prev(self):
        self.__pointer -= 1
        self.__pointer %= self.__length
        return self

    def __prev__(self):
        return self.prev()

    def __call__(self):
        return self.__playlist[self.__pointer]

    def __iter__(self):
        return self

playlist = playlists([k for k in for_playlist_comprehention("conf.txt")])

def main():
    print('''\
    내 앱에 필요한 정도반 적을거임.

    # mpv 사용법

    이 사용법은 최대한 간단히 말했으니 알아서 CLI에서 살아남으세요. (제가 쓰려고 만든거라, 코드도 구리고, 이 메세지는 앱 실행시 맨날  뜨고, 종료 후 재실행시 다시 볼수 있습니다. 즉, 지금 한번밖에 못보죠. 🔥 강해져야합니다. 🔥)

    "살아남았다는건, 강하다는것."

    ---

     * `L` : 🔂 현제 곡 반복재생 (on/off)
     * `l` : `A]•--•[B` 구간반복 (**클릭 시** `*`, `A*¹ -> B*²`순서로 지정되어서 구간반복. **구간반복중에** 누르면 **clear (구간 반복 해제)**
     * `9` : 🔉  VOLUME ⬇️
     * `0` : 🔊 VOLUME ⬆️
     * `m` : 🔇 MUTE • CANCLE MUTE
     * space key : ⏸️ 일시정지 • ▶️ 재계 (⚠️  N.B. `p`버튼도 이 기능을 함 ⚠️)
     * `[` : 재생속도 감소 (감속)
     * `]` : 재생속도 증가 (배속 (엄밀히는 가속))
     * `q` : 종료 (⚠️ N.B. 에초에 재생하려는 대상이 긑나면 종료됨 ⚠️)
     * ⬅️ (왼쪽 화살표 모양 조작 버튼) : 5s 전으로
     * ➡️ (오른쪽 화살표 모양 조작 버튼) : 5s 후로
     * ⬆️ (윗쪽 화살표 모양 조작 버튼) : 1 min 후로
     * ⬇️ (아랫쪽 화살표 모양 조작 버튼) : 1 min 전으로

    ---

    TIP : 종료시 `Exiting...`이라고 뜨는데, 이게 보이면 이미 mpv는 종료된겁니다. 다시 처음으로 못가요.\
    ''')
    mp3player_remote_controller()
    ultimite_quit_controll_toggle() # 시
    if not quit_signal:
        mp3player_remote_controller()
        ultimite_quit_controll_toggle() # 발
        if quit_signal:
            return
        for k in playlist:
            mp3player_remote_controller()
            ultimite_quit_controll_toggle() # 제
            if quit_signal: break
            mp3player_remote_controller()
            ultimite_quit_controll_toggle() # 발
            if quit_signal: break
            mp3_play_control_tower(k)
            ultimite_quit_controll_toggle() # 멈
            if quit_signal: break
            ultimite_quit_controll_toggle() # 추
            if quit_signal: break
            print(f'# ===== [ "{k()}" - audio played by mpv ] ===== #')
            s(f'mpv "{k()}"')
            mp3player_remote_controller()
            ultimite_quit_controll_toggle() # 라
            if quit_signal: break
            mp3player_remote_controller()
            ultimite_quit_controll_toggle() # 고
            if quit_signal: break
            mp3player_remote_controller()
            for _ in range(25):
                ultimite_quit_controll_toggle() #야!!!!
                sl(0.015)
            for _ in range(25):
                mp3player_remote_controller() #야!!!!
                sl(0.015)
            if quit_signal: break
            ultimite_quit_controll_toggle() # 제
            if quit_signal:break
            mp3player_remote_controller()
            ultimite_quit_controll_toggle() # 발
            if quit_signal: break
            ultimite_quit_controll_toggle() # 좀
            if quit_signal: break
            ultimite_quit_controll_toggle() # 갈!
            if quit_signal: break
            for _ in range(25):
                ultimite_quit_controll_toggle() #야!!!!
                sl(0.015)
            if quit_signal: break
            for _ in range(25):
                mp3player_remote_controller() #야!!!!
                sl(0.015)
            for _ in range(25):
                ultimite_quit_controll_toggle() #야!!!!
                sl(0.015)
            if quit_signal: break
            for _ in range(25):
                mp3player_remote_controller() #야!!!!
                sl(0.015)

    # ultimite_quit_controll_toggle() for stop programm more easier

if __name__ == "__main__": main() #Sucks. danguerus app