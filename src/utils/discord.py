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