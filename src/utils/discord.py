from src import *

class discord:
    # Not leaking my hard work database :sob:
    INVALID_JSON = '50109'
    INVALID_JSON_2 = '50035'
    INTERACTION_FAILED = '110000'
    BANNED_TOKEN = '40007'
    LOCKED_TOKEN = '40002'
    DEAD_ACCOUNT = '401'
    LOCKED_ACCOUNT = 'You need to verify'
    UNKNOWN_ACCOUNT = '40001'
    LIMITED = '20028'
    RETRY_AFTER_LIMITED = 'retry_after'
    API_BAN = 'You are being blocked from accessing our API'
    CLOUDFLARE = 'Cloudflare'
    AUTOMOD_FLAGGED = '200000'
    MESSAGE_BLOCKED_BY_CONTENT_FILTER = '50022'
    NO_ACCESS_NOT_INSIDE = '50001'
    MISSING_PERMISSIONS = '50013'
    ACTION_NOT_ALLOWED = '50007'
    VERIFICATION_TOO_HIGH = '50009'
    INVALID_SERVER = '50055'
    UNKNOWN_SERVER = '10005'
    NOT_IN_SERVER = 'Unknown Guild'
    SERVER_LIMITED_VIOLATED_TOS = '400002'
    MAX_SERVERS = '30001'
    ALREADY_A_MEMBER = '150009'
    UNKNOWN_INVITE = 'Unknown Invite'
    CHANNEL_NOT_FOUND = '50034'
    UNKNOWN_CHANNEL = '10003'
    CANT_DO_THAT_ON_THIS_CHANNEL = '50024'
    UNABLE_TO_SEND = '50008'
    CANT_SEND_EMPTY_MESSAGE = '50046'
    INVALID_MESSAGE_TYPE = '50018'
    INVALID_MESSAGE_CONTENT = '40004'
    MUTED_ACCESS_TO_SEND_MESSAGES_LIMITED_BY_SERVER = '340013'
    UNKNOWN_EMOJI = '10014'
    MAX_REACTIONS_ON_MESSAGE = '30010'
    REACTION_WAS_BLOCKED = '40060'
    ONBOARDING_NOT_NEEDED = 'Onboarding responses are not valid'

    def cleaninvite(invite):
        pattern = r'(?:(?:https?:\/\/)?(?:www\.)?(?:discord\.(?:gg|com)|discordapp\.com)\/(?:invite\/|channels\/@me\/)?)?([a-zA-Z0-9\-_]+)'
        
        match: re.Match = re.search(pattern, invite, re.IGNORECASE)
        if match:
            return match.group(1)
    
    # dont question im too lazy to replace the func everywhere
    def sleep(tosleep):
        try:
            time.sleep(float(tosleep))
        except:
            pass

    def getid(token) :
        period = token.find('.')
        if period != -1: 
            cut = token[:period]
        return base64.b64decode(cut + '==').decode()
    
    def getnonce():
        discord_epoch = 1420070400000
        timestamp = int(time.time() * 1000)
        nonce = (timestamp - discord_epoch) << 22
        return str(nonce)
    
    def makepings(ids, amt):
        if amt == 0:
            return ''
        shuffled = ids[:]  
        random.shuffle(shuffled)
        selected = shuffled[:min(amt, len(shuffled))]
        return ' '.join(f'<@{userid}>' for userid in selected)

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
    

    # Not leaking my hard work database :sob:
    def errordatabase(text):
        db = {
            discord.INVALID_JSON: 'Invalid JSON (please check what you pasted)',
            discord.INVALID_JSON_2: 'Invalid JSON (please check what you pasted)',
            discord.INTERACTION_FAILED: 'Interaction failed',
            discord.BANNED_TOKEN: 'Banned token',
            discord.LOCKED_TOKEN: 'Account locked',
            discord.DEAD_ACCOUNT: 'Dead account',
            discord.LOCKED_ACCOUNT: 'Locked account',
            discord.UNKNOWN_ACCOUNT: 'Unknown account',
            discord.LIMITED: 'Limited',
            discord.RETRY_AFTER_LIMITED: 'Limited',
            discord.API_BAN: 'API BAN',
            discord.CLOUDFLARE: 'Cloudflare',
            discord.AUTOMOD_FLAGGED: 'Automod flagged',
            discord.MESSAGE_BLOCKED_BY_CONTENT_FILTER: 'Message blocked by content filter',
            discord.NO_ACCESS_NOT_INSIDE: 'No access',
            discord.MISSING_PERMISSIONS: 'Missing permissions',
            discord.ACTION_NOT_ALLOWED: 'Action not allowed',
            discord.VERIFICATION_TOO_HIGH: 'Verification too high (server requires PV, EV or being in server for 10 mins)',
            discord.INVALID_SERVER: 'Invalid server',
            discord.UNKNOWN_SERVER: 'Unknown server',
            discord.NOT_IN_SERVER: 'Not in server',
            discord.SERVER_LIMITED_VIOLATED_TOS: 'Server is limited/voliated discords tos',
            discord.MAX_SERVERS: 'Max servers',
            discord.ALREADY_A_MEMBER: 'Alerdy a member (no need to verify)',
            discord.UNKNOWN_INVITE: 'Unknown Invite',
            discord.CHANNEL_NOT_FOUND: 'Channel not found',
            discord.UNKNOWN_CHANNEL: 'Unknown channel',
            discord.CANT_DO_THAT_ON_THIS_CHANNEL: 'Cant do that on this channel',
            discord.UNABLE_TO_SEND: 'Unable to send',
            discord.CANT_SEND_EMPTY_MESSAGE: 'Cant send empty message',
            discord.INVALID_MESSAGE_TYPE: 'Invalid message type',
            discord.INVALID_MESSAGE_CONTENT: 'Invalid message content',
            discord.MUTED_ACCESS_TO_SEND_MESSAGES_LIMITED_BY_SERVER: 'Muted/Access to send messages limited by server',
            discord.UNKNOWN_EMOJI: 'Unknown emoji',
            discord.MAX_REACTIONS_ON_MESSAGE: 'Max reactions on message',
            discord.REACTION_WAS_BLOCKED: 'Reaction was blocked',
            discord.ONBOARDING_NOT_NEEDED: 'No need to bypass onboarding',
        }

        for key, message in db.items():
            if key in text:
                return message, key

        if isinstance(text, str):
            try:
                import json
                text = json.loads(text)
            except:
                return text, None

        if isinstance(text, dict) and 'message' in text:
            return text['message'], None

        return text, None