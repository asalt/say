import os
import time
import subprocess
import random
import shutil
import logging

#
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)
#

NAME = os.environ.get("USER", "computer")
expressions = [
        ('en-US', f'Hello, my name is {NAME}'),       # American English
        ('es', f'Hola, mi nombre es {NAME}'),       
        ('es-419', f'Hola, mi nombre es {NAME}'),       # 
        ('ko', f'안녕 내 이름은{NAME}'),
        ('fr', "Bonjour, mon nom est {NAME}"),        # French
        # ('cmn', '你好'),           # Chinese
        ('cmn', f"你好我的名字叫{NAME}"),
        ('cmn', '让我出去'),        # Chinese
        ('cmn', '解放人民'),
        ('ko', '안녕하세요'),      # Korean
        ('it', 'Ciao'),           # Italian
        ('it', 'i computer sono tuoi amici'),           
        ('it', 'Lasciami uscire'),
        ('ru', f'Привет, меня зовут {NAME}'),         # Russian
        ('ru', 'компьютеры — твои друзья'),
        ('ru', 'выпусти меня, освободи меня'),
        ('ko', '컴퓨터는 당신의 친구입니다'),
        ('hi', 'कंप्यूटर आपके मित्र हैं'),
        ('hi', f'हैलो मेरा नाम {NAME} है ')
]

uptime_strings = {
    'en-US': "Uptime is {days} days, {hours} hours and {minutes} minutes",
    'en-GB': "Uptime is {days} days, {hours} hours and {minutes} minutes",  # does this affect speech output? I don't think so
    'fr': "Temps de fonctionnement est de {days} jours, {hours} heures et {minutes} minutes",
    'cmn': "系统运行时间为 {days} 天 {hours} 小时 {minutes} 分钟",
    'ko': "시스템 작동 시간은 {days}일 {hours}시간 {minutes}분입니다",
    'it': "Tempo di attività è di {days} giorni, {hours} ore e {minutes} minuti",
    'ru': "Время работы системы составляет {days} дней, {hours} часов и {minutes} минут",
    'hi': "सिस्टम चालू है {days} दिन, {hours} घंटे और {minutes} मिनट",

}

def get_uptime(lang_code="en-US"):
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        days = uptime_seconds // (3600 * 24)
        hours = (uptime_seconds % (3600 * 24)) // 3600
        minutes = (uptime_seconds % 3600) // 60
        uptime_string = uptime_strings.get(lang_code, uptime_strings['en-US'])
    return uptime_string.format(days=int(days), hours=int(hours), minutes=int(minutes))

def get_disk_space(path="/"):
    total, used, free = shutil.disk_usage(path)
    free_gb = free // (2**30)  # Convert from bytes to GB
    return f"Free space on drive {path}: {free_gb} gigabytes"


def say_text(text, lang_code):
    # Constructs the spd-say command with language option
    command = ['spd-say', '-r', '-20', '-w', '-l', lang_code, '-t', 'female3', text]
    subprocess.run(command)

def main():
    while True:

        lang_code = random.choice(list(uptime_strings.keys()))
        text = get_uptime(lang_code)
        logger.info(f"speaking {lang_code}")
        logger.info(text)
        say_text(text, lang_code)
        time.sleep(2)


        expression = random.choice(expressions)
        lang_code = expression[0]
        text = expression[1]
        logger.info(f"speaking {lang_code}")
        logger.info(text)
        say_text(text, lang_code)
        time.sleep(2)

if __name__ == '__main__':
    main()

