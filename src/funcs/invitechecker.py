from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.threading import threading
from src.utils.discord import discord
from src.utils.logging import logger
from src.utils.sessionmanager import client as Client

class invitechecker:
    def __init__(self):
        self.console = console('Invite Checker')
        os.makedirs('data\\invitechecker', exist_ok=True)
        timestamp = dt.now().strftime('%Y-%m-%d--%H-%M-%S')
        self.sortingpath = 'data\\invitechecker\\' + timestamp
        self.valids = []
        self.invalids = []

    def check(self, client: Client, invite):
        try:
            regex = discord.cleaninvite(invite)
            fullinvite = 'https://discord.com/invite/' + discord.cleaninvite(invite)

            while True:
                r = client.sess.get(
                    f'https://discord.com/api/v9/invites/{regex}',
                    headers=client.headers,
                    params = {
                        'inputValue': invite,
                        'with_counts': 'true',
                        'with_expiration': 'true',
                        'with_permissions': 'false'
                    }
                )

                if r.status_code == 200:
                    data = r.json()
                    server = dict(data.get('guild', {}))
                    features = list(server.get('features', []))

                    members = data.get('approximate_member_count', 0)
                    boosts = server.get('premium_subscription_count', 0)
                    features = []

                    if 'GUILD_ONBOARDING' in features:
                        if 'Onboarding' not in features:
                            features.append('Onboarding')

                    if 'MEMBER_VERIFICATION_GATE_ENABLED' in features:
                        if 'Rules' not in features:
                            features.append('Rules')

                    if 'AUTO_MODERATION' in features:
                        if 'AutoMod' not in features:
                            features.append('AutoMod')

                    if features:
                        extra = f' {" ".join(features)}'
                    else:
                        extra = ''

                    logger.success(f'{fullinvite} » {extra} {members} Members {boosts} Boosts')
                    self.valids.append(fullinvite)
                    break

                elif 'retry_after' in r.text:
                    ratelimit = r.json().get('retry_after', 1.5)
                    logger.ratelimit(f'{fullinvite} » {ratelimit}s')
                    discord.sleep(ratelimit)

                elif 'Try again later' in r.text:
                    logger.ratelimit(f'{fullinvite} » 5s')
                    discord.sleep(5)

                elif 'Cloudflare' in r.text:
                    logger.cloudflare(f'{fullinvite} » 10s')
                    discord.sleep(10)

                elif 'You need to verify' in r.text:
                    logger.locked(f'{client.maskedtoken} Locked/Flagged')
                    self.invalids.append(fullinvite)
                    break

                else:
                    e, etype = discord.errordatabase(r.text)
                    logger.error(f'{fullinvite} » Invite INVALID')
                    self.invalids.append(fullinvite)
                    break

        except Exception as e:
            logger.error(f'{client.maskedtoken} » {e}')
            self.invalids.append(fullinvite)

    def run(self, invite):
        client = Client()
        self.check(client, invite)

    def menu(self):
        self.console.prep()

        logger.info('Choose a file with invites (if you dont have them you can use the invite scraper from scraping menu)')
        invitesfile = files.choosefile()
        if not os.path.exists(invitesfile):
            logger.error('File does not exist')
            return

        with open(invitesfile, 'r') as f:
            invites = f.read().splitlines()

        logger.info('Use fast only if you have less than 50 invites or have proxies')
        mode = self.console.input('Checker mode (1=Fast, 2=Optimized', int)
        self.delay = self.console.input('Delay', float)
        logger.info(f'Stats will be saved to {self.sortingpath}')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')

        if mode == 1:
            threading(
                func=self.run,
                tokens=invites,
                delay=self.delay,
                passed='Invites'
            )
        else:
            def optiimzedrunner():
                for inivte in invites:
                    invites.remove(inivte)
                    self.run(inivte)
                    discord.sleep(self.delay)

            threads = []
            for _ in range(2):
                t=threadinglib.Thread(target=optiimzedrunner)
                t.start()
                threads.append(t)
            
            for t in threads:
                t.join()

        os.makedirs(self.sortingpath, exist_ok=True)
        valids_path = self.sortingpath + '\\valids.txt'
        with open(valids_path, 'w') as f:
            f.write('\n'.join(self.valids))

        invalids_path = self.sortingpath + '\\invalids.txt'
        with open(invalids_path, 'w') as f:
            f.write('\n'.join(self.invalids))


        os.system(f'start {self.sortingpath}')
