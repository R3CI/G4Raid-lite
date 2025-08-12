# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged


from src import *

class discord:
    def cleaninvite(invite):
        pattern = r'(?:(?:https?:\/\/)?(?:www\.)?(?:discord\.(?:gg|com)|discordapp\.com)\/(?:invite\/|channels\/@me\/)?)?([a-zA-Z0-9\-_]+)'
        
        match: re.Match = re.search(pattern, invite, re.IGNORECASE)
        if match:
            return match.group(1)
        
    def sleep(tosleep):
        try:
            time.sleep(float(tosleep))
        except:
            pass
    
    def getnonce():
        discordepoch = 1420070400000
        timestamp = int(time.time() * 1000)
        nonce = (timestamp - discordepoch) << 22
        return str(nonce)

    def getemoji(length):
        emoji_ranges = [
            (0x1F600, 0x1F64F),
            (0x1F300, 0x1F5FF),
            (0x1F680, 0x1F6FF),
            (0x1F700, 0x1F77F),
            (0x1F900, 0x1F9FF),
        ]
        emojis = [chr(code) for start, end in emoji_ranges for code in range(start, end + 1)]
        return ''.join(random.choices(emojis, k=length))

    def getstring(length):
        return ''.join(random.choices(string.digits, k=length))
    

    def errordatabase(text):
        # Database in PAID only bc of skids
        return text, None