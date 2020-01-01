from typing import Dict, List, Optional

from mee6_py_api.utils.logging import BaseLoggingService

class Levels(BaseLoggingService):
    def __init__(self, base_API):
        self.base_API = base_API

        self.base_url = "{}plugins/levels/".format(self.base_API.base_url)

        # List of leaderboard pages saved from the previous request
        self.leaderboard_pages_cache = []

    async def get_leaderboard_page(self, page: int = 0, guild_id: int = None) -> Dict:
        self.logger.debug('running get_leaderboard_page for page {}'.format(page))
        if guild_id is None:
            guild_id = self.base_API.default_guild_id

        url = "{}leaderboard/{}".format(self.base_url, guild_id)
        result = await self.base_API.send_get_request_and_get_response(url, {'page': page})
        return result

    async def get_all_leaderboard_pages(self, page_count_limit = 20, guild_id: int = None) -> List[Dict]:
        self.logger.debug('running get_all_leaderboard_pages')
        self.leaderboard_pages_cache = []

        for i in range(page_count_limit):
            leaderboard_page = await self.get_leaderboard_page(i, guild_id)
            if len(leaderboard_page['players']) > 0:
                self.leaderboard_pages_cache.append(leaderboard_page)
            else:
                break

        return self.leaderboard_pages_cache

    async def get_user_details(self, user_id: int, guild_id: int = None, dont_use_cache = False, page_count_limit = 20) -> Dict:
        self.logger.debug('running get_user_details for user_id {}'.format(user_id))
        if guild_id is None:
            guild_id = self.base_API.default_guild_id

        if dont_use_cache:
            leaderboard_pages = await self.get_all_leaderboard_pages(page_count_limit = page_count_limit, guild_id=guild_id)
        else:
            leaderboard_pages = self.leaderboard_pages_cache
            if len(leaderboard_pages) == 0:
                leaderboard_pages = await self.get_all_leaderboard_pages(page_count_limit = page_count_limit, guild_id=guild_id)

        for leaderboard_page in leaderboard_pages:
            for player in leaderboard_page['players']:
                if int(player['id']) == int(user_id):
                    return player


    async def get_user_xp(self, user_id: int, guild_id: int = None, dont_use_cache = False, page_count_limit = 20) -> int:
        user_details = await self.get_user_details(user_id, guild_id, dont_use_cache, page_count_limit)
        if user_details is not None:
            return int(user_details['xp'])

    async def get_user_level(self, user_id: int, guild_id: int = None, dont_use_cache = False, page_count_limit = 20) -> int:
        user_details = await self.get_user_details(user_id, guild_id, dont_use_cache, page_count_limit)
        if user_details is not None:
            return int(user_details['level'])


