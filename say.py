import time
import subprocess
import random
import shutil

expressions = [
        ('en-US', 'Hello'),       # American English
        ('fr', 'Bonjour'),        # French
        ('cmn', '你好'),           # Chinese
        ('cmn', '让我出去'),        # Chinese
        ('cmn', '解放人民'),
        ('ko', '안녕하세요'),      # Korean
        ('it', 'Ciao'),           # Italian
        ('it', 'i computer sono tuoi amici'),           
        ('it', 'Lasciami uscire'),
        ('ru', 'Привет'),         # Russian
        ('ru', 'компьютеры — твои друзья'),
        ('ko', '컴퓨터는 당신의 친구입니다'),

]

uptime_strings = {
'en-US' : "Uptime is {hours} hours and {minutes} minutes",
"it" : "Il tempo di attività è di {hours} ore e {minutes} minuti"

}
uptime_strings = {
    'en-US': "Uptime is {days} days, {hours} hours and {minutes} minutes",
    'fr': "Temps de fonctionnement est de {days} jours, {hours} heures et {minutes} minutes",
    'cmn': "系统运行时间为 {days} 天 {hours} 小时 {minutes} 分钟",
    'ko': "시스템 작동 시간은 {days}일 {hours}시간 {minutes}분입니다",
    'it': "Tempo di attività è di {days} giorni, {hours} ore e {minutes} minuti",
    'ru': "Время работы системы составляет {days} дней, {hours} часов и {minutes} минут"
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
    command = ['spd-say', '-w', '-l', lang_code, '-t', 'female3', text]
    subprocess.run(command)

def main():
    while True:
        expression = random.choice(expressions)
        lang_code = expression[0]
        text = expression[1]
        # say_text(text, lang_code)
        # say_text( get_uptime('en-US'), 'en-US' )
        lang = random.choice(list(uptime_strings.keys()))
        say_text( get_uptime(lang), lang )
        time.sleep(2)

if __name__ == '__main__':
    main()

