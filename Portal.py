from colorama import init, Fore, Style
import time
import os
import subprocess

init(autoreset=True)

# лого
logo = r"""
             ,-:;//;:=, .
          . :H@@@MM@M#H/.,+%;,
       ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=             .---=-=:=,.
  =@#@@@MX.,                -%HX$$%%%:;
 =-./@M@M$                   .;@MMMM@MM:
 X@/ -$MM/                    . +MM@@@M$
,@M@H: :@:                    . =X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; =;
  /%+%$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@= =,
               =++%%%%+/:-.
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_orange(text):
    print(Fore.YELLOW + Style.BRIGHT + text)

clear_screen()
print_orange(logo)
print(Fore.YELLOW + Style.BRIGHT + "               APERTURE SCIENCE ENRICHMENT CENTER")
print(Fore.YELLOW + Style.BRIGHT + "               'Want You Gone' Protocol Activated")
time.sleep(2)

# === ПУТЬ К ПЕСНЕ ===
song_path = r"C:\Users\MARS\Desktop\Aperture Since\Want,you gone.mp3"

try:
    subprocess.Popen(['start', '', song_path], shell=True)
except Exception as e:
    print(Fore.RED + f"Ошибка :( {e}")

# Начало
initial_delay = 5.0 
time.sleep(initial_delay)

# Задержка строк и текст
lyrics = [
    (0, "Well here we are again"),
    (3.5, "It's always such a pleasure"),
    (7, "Remember when you tried"),
    (8, "to kill me twice?"),
    (11, "Oh how we laughed and laughed"),
    (13, "Except I wasn't laughing"),
    (16, "Under the circumstances"),
    (18, "I've been shockingly nice"),
    (20.2, "You want your freedom?"),
    (23.5, "Take it"),
    (26.7, "That's what I'm counting on"),
    (30, "I used to want you dead"),
    (34, "but"),
    (35, "Now I only want you gone"),
    (42, "She was a lot like you"),
    (44.1, "(Maybe not quite as heavy)"),
    (47, "Now little Caroline is in here too"),
    (52, "One day they woke me up"),
    (54.8, "So I could live forever"),
    (57.7, "It's such a shame the same"),
    (59, "will never happen to you"),
    (62, "You've got your"),
    (64, "short sad life left"),
    (67.5, "That's what I'm counting on"),
    (72, "I'll let you get right to it"),
    (75.5, "Now I only want you gone"),
    (83.5, "Goodbye my only friend"),
    (86, "Oh, did you think I meant you?"),
    (88.5, "That would be funny"),
    (90, "if it weren't so sad"),
    (93, "Well you have been replaced"),
    (95, "I don't need anyone now"),
    (98, "When I delete you maybe"),
    (100, "I'll stop feeling so bad"),
    (103, "Go make some new disaster"),
    (107.6, "That's what I'm counting on"),
    (112, "You're someone else's problem"),
    (117, "Now I only want you gone"),
    (121, "Now I only want you gone"),
    (126, "Now I only want you gone"),
    (131, ""),
]

print(Fore.YELLOW + "Loading...")

start_time = time.time()
for delay, line in lyrics:
    elapsed = time.time() - start_time
    wait = delay - elapsed
    if wait > 0:
        time.sleep(wait)
    print_orange(line.center(80))

print(Fore.YELLOW + Style.BRIGHT + "Торт может быть ложью... но продолжай бороться!")