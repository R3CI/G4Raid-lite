from src import *
from src.utils.console import console
from src.utils.discord import discord
from src.utils.logging import logger
from src.utils.sessionmanager import client as Client

class inviteinfo:
    def __init__(self):
        self.console = console('Invite Info')
        self.invite = None
        self.info = None
    
    def get(self, client: Client):
        try:
            while True:
                r = client.sess.get(
                    f'https://discord.com/api/v9/invites/{self.invite}?inputValue={self.invite}&with_counts=true&with_expiration=true',
                    headers=client.headers
                )

                if r.status_code == 200:
                    logger.success('Got info')
                    self.info = r.json()
                    break

                elif 'retry_after' in r.text:
                    ratelimit = r.json().get('retry_after', 1.5)
                    logger.ratelimit(f'{ratelimit}s')
                    discord.sleep(ratelimit)

                elif 'Try again later' in r.text:
                    logger.ratelimit('5s')
                    discord.sleep(5)

                elif 'Cloudflare' in r.text:
                    logger.cloudflare('10s')
                    discord.sleep(10)

                elif 'You need to verify' in r.text:
                    logger.locked('Locked/Flagged')
                    break

                else:
                    e, etype = discord.errordatabase(r.text) 
                    logger.error(e)
                    break

        except Exception as e:
            logger.error(e)

    def printinfo(self):
        server = self.info.get('guild', {})
        channel = self.info.get('channel', {})
        profile = self.info.get('profile', {})
        logger.info(f'Server Name » {server.get("name")}')
        logger.info(f'Server ID » {server.get("id")}')
        logger.info(f'Server Description » {server.get("description")}')
        logger.info(f'Server Verification Level » {server.get("verification_level")}')
        logger.info(f'Vanity URL Code » {server.get("vanity_url_code") or "None"}')
        logger.info(f'Server NSFW Enabled » {server.get("nsfw")}')
        logger.info(f'Server NSFW Level » {server.get("nsfw_level")}')
        logger.info(f'Server Boosts » {server.get("premium_subscription_count")}')
        logger.info(f'Server Boost Tier » {server.get("premium_tier")}')
        logger.info(f'Server Icon Hash » {server.get("icon")}')
        logger.info(f'Server Banner Hash » {server.get("banner")}')
        logger.info(f'Server Splash Hash » {server.get("splash")}')

        logger.info(f'Channel Name » {channel.get("name")}')
        logger.info(f'Channel ID » {channel.get("id")}')
        logger.info(f'Channel Type » {channel.get("type")}')

        logger.info(f'Profile Name » {profile.get("name")}')
        logger.info(f'Profile ID » {profile.get("id")}')
        logger.info(f'Profile Description » {profile.get("description")}')
        logger.info(f'Profile Tag » {profile.get("tag")}')
        logger.info(f'Members » {profile.get("member_count")}')
        logger.info(f'Online Now » {profile.get("online_count")}')
        logger.info(f'Profile Badge » {profile.get("badge")}')
        logger.info(f'Profile Badge Hash » {profile.get("badge_hash")}')
        logger.info(f'Primary Badge Color » {profile.get("badge_color_primary")}')
        logger.info(f'Secondary Badge Color » {profile.get("badge_color_secondary")}')
        logger.info(f'Primary Brand Color » {profile.get("brand_color_primary")}')
        logger.info(f'Custom Banner Hash » {profile.get("custom_banner_hash")}')
        logger.info(f'Banner Hash » {profile.get("banner_hash")}')
        logger.info(f'Icon Hash » {profile.get("icon_hash")}')
        logger.info(f'Visibility Level » {profile.get("visibility")}')
        logger.info(f'Profile Premium Tier » {profile.get("premium_tier")}')
        logger.info(f'Profile Boosts » {profile.get("premium_subscription_count")}')

        logger.info('Server Features:')
        for f in server.get('features', []):
            readable = f.replace('_', ' ').title()
            logger.info(f'- {readable}')

        logger.info('Profile Features:')
        for f in profile.get('features', []):
            readable = f.replace('_', ' ').title()
            logger.info(f'- {readable}')

        logger.info('Game Application IDs:')
        for app_id in profile.get('game_application_ids', []):
            logger.info(f'- {app_id}')

        logger.info('Game Activity:')
        for app_id, activity in profile.get('game_activity', {}).items():
            level = activity.get('activity_level')
            score = activity.get('activity_score')
            logger.info(f'- App ID {app_id} » Level: {level}, Score: {score}')

        logger.info('Profile Traits:')
        for trait in profile.get('traits', []):
            emoji = trait.get('emoji_name')
            animated = trait.get('emoji_animated')
            label = trait.get('label')
            logger.info(f'- {emoji} ({animated}) » {label}')

        logger.info(f'Approximate Member Count » {self.info.get("approximate_member_count")}')
        logger.info(f'Approximate Presence Count » {self.info.get("approximate_presence_count")}')

    def run(self):
        client = Client()
        self.get(client)
        if self.info:
            self.printinfo()

    def menu(self):
        self.console.prep()
        self.invite = self.console.input('Invite', str)
        self.invite = discord.cleaninvite(self.invite)
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')

        self.run()
        
