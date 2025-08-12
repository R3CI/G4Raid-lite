# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged


from src import *
from src.utils.config import get

class logger:
    def timestamp():
        return dt.now().strftime('%H:%M:%S ')

    def info(text, text2=None):
        if text2:
            first = f'{co.main}[{co.reset}{text2}{co.main}] {co.reset}»{co.reset} '
        else:
            first = ''

        log = f'{co.main}[{co.reset}{text}{co.main}]{co.reset}'

        for char in ['»', '«']:
            log = log.replace(char, f'{co.main}{char}{co.reset}')

        log = f'{first}{log}'
            
        print(log)

    def success(text):
        log = f'{co.black}{logger.timestamp()}{co.success}SUCCESS {co.reset}»{co.reset} {co.success}[{text}]{co.reset}'

        for char in ['»', '«']:
            log = log.replace(char, f'{co.reset}{char}{co.success}')
            
        print(log)

    def error(text):                                      
        log = f'{co.black}{logger.timestamp()}{co.error}ERROR {co.reset}»{co.reset} {co.error}[{text}]{co.reset}'

        for char in ['»', '«']:
            log = log.replace(char, f'{co.reset}{char}{co.error}')
            
        print(log)

    def locked(text):                                      
        log = f'{co.black}{logger.timestamp()}{co.locked}LOCKED {co.reset}»{co.reset} {co.locked}[{text}]{co.reset}'

        for char in ['»', '«']:
            log = log.replace(char, f'{co.reset}{char}{co.locked}')
            
        print(log)

    def debug(text): 
        if get.debug.enabled():                                     
            log = f'{co.black}{logger.timestamp()}{co.debug}DEBUG {co.reset}»{co.reset} {co.debug}[{text}]{co.reset}'

            for char in ['»', '«']:
                log = log.replace(char, f'{co.reset}{char}{co.debug}')
                
            print(log)

    def warning(text):                                      
        log = f'{co.black}{logger.timestamp()}{co.warning}WARNING {co.reset}»{co.reset} {co.warning}[{text}]{co.reset}'

        for char in ['»', '«']:
            log = log.replace(char, f'{co.reset}{char}{co.warning}')
            
        print(log)

    def ratelimit(text):                                      
        log = f'{co.black}{logger.timestamp()}{co.ratelimit}RATELIMIT {co.reset}»{co.reset} {co.ratelimit}[{text}]{co.reset}'

        for char in ['»', '«']:
            log = log.replace(char, f'{co.reset}{char}{co.ratelimit}')
            
        print(log)

    def cloudflare(text):                                      
        log = f'{co.black}{logger.timestamp()}{co.cloudflare}CLOUDFLARE {co.reset}»{co.reset} {co.cloudflare}[{text}]{co.reset}'

        for char in ['»', '«']:
            log = log.replace(char, f'{co.reset}{char}{co.cloudflare}')
            
        print(log)

    def captcha(text):                                      
        log = f'{co.black}{logger.timestamp()}{co.captcha}CAPTCHA {co.reset}»{co.reset} {co.captcha}[{text}]{co.reset}'

        for char in ['»', '«']:
            log = log.replace(char, f'{co.reset}{char}{co.captcha}')
            
        print(log)
