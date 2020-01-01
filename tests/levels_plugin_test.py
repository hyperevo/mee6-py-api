from mee6_py_api.api import API
import asyncio
from pprint import pprint

from mee6_py_api.utils.logging import setup_logger


class TestClass:
    def __init__(self):
        self.mee6API = API()

    async def run_tests(self):
        #await self.test_get_leaderboard_page()
        #await self.test_get_all_leaderboard_pages()
        await self.test_get_user_details()
        #await self.test_get_user_xp()
        #await self.test_get_user_level()

    async def test_get_leaderboard_page(self):
        leaderboard_page = await self.mee6API.levels.get_leaderboard_page()
        pprint(leaderboard_page)

    async def test_get_all_leaderboard_pages(self):
        leaderboard_pages = await self.mee6API.levels.get_all_leaderboard_pages()
        pprint(leaderboard_pages)

    async def test_get_user_details(self):
        user_details = await self.mee6API.levels.get_user_details(265009449222012929, page_count_limit=1)
        pprint(user_details)

    async def test_get_user_xp(self):
        user_details = await self.mee6API.levels.get_user_xp(265009449222012929, page_count_limit=1)
        pprint(user_details)

    async def test_get_user_level(self):
        user_details = await self.mee6API.levels.get_user_level(265009449222012929, page_count_limit=1)
        pprint(user_details)



if __name__ == "__main__":
    __spec__ = 'None'
    setup_logger()
    testClass = TestClass()

    loop = asyncio.get_event_loop()
    asyncio.ensure_future(testClass.run_tests())
    loop.run_forever()
    loop.close()