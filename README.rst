====================
Mee6 Python API
====================

.. image:: https://img.shields.io/badge/python-3.6-blue.svg
    :target: https://www.python.org/downloads/release/python-360/
    :alt: Python3.6



This is the unofficial python API for mee6.

This implements the api as per the Mee6 API docs located here: https://github.com/SilBoydens/Mee6-api-docs

This API is asynchronous.

Installation
============

::

    pip install mee6-py-api

Usage
=====

First, import the package and create the API class. Replace your_guild_id with your guild id.


.. code-block:: Python

    from mee6_py_api import API
    mee6API = API(your_guild_id)

Examples
~~~~~~~~~~~~~~~~~~~~~~~

See the tests folder for some functional examples

Get a leaderboard page
+++++++++++++++++++++++++

Leaderboards are separated into pages of 100 users. Pages start at 0.

.. code-block:: Python

    leaderboard_page = await mee6API.levels.get_leaderboard_page(0)
    print(leaderboard_page)

Example of what it will return:

::


    {'admin': False,
     'banner_url': None,
     'guild': {'icon': 'd25eb4a577ab711df2e20b6b15158561',
               'id': '446075987680165888',
               'name': 'Helios Protocol',
               'premium': False},
     'page': 0,
     'player': None,
     'players': [
                 {'avatar': 'e23737d84c718554c7894e2d3a827051',
                  'detailed_xp': [1230, 1255, 7005],
                  'discriminator': '9597',
                  'guild_id': '446075987680165888',
                  'id': '300302688346832897',
                  'level': 11,
                  'message_count': 350,
                  'username': 'johnny',
                  'xp': 7005},
                 {'avatar': 'e7ec097ad84062ce77211b3393910d62',
                  'detailed_xp': [832, 1255, 6607],
                  'discriminator': '0098',
                  'guild_id': '446075987680165888',
                  'id': '450024877710245889',
                  'level': 11,
                  'message_count': 330,
                  'username': 'timmy',
                  'xp': 6607},
                ...
                 ],
     'role_rewards': [{'rank': 10,
                       'role': {'color': 6323595,
                                'hoist': False,
                                'id': '456256644905697283',
                                'managed': False,
                                'mentionable': False,
                                'name': 'Active Community Member',
                                'permissions': 104189505,
                                'position': 14}},
                      {'rank': 17,
                       'role': {'color': 14051342,
                                'hoist': True,
                                'id': '456256766921932802',
                                'managed': False,
                                'mentionable': False,
                                'name': 'Superstar',
                                'permissions': 104189505,
                                'position': 18}}],
     'user_guild_settings': None,
     'xp_per_message': [15, 25],
     'xp_rate': 1.0}

Get mee6 details of a user
+++++++++++++++++++++++++++

Replace user_id with your user id.

.. code-block:: Python

    details = await mee6API.levels.get_user_details(user_id)
    print(details)

Example of what it will return:

::


     {'avatar': 'e7ec097ad84062ce77211b3393910d62',
      'detailed_xp': [832, 1255, 6607],
      'discriminator': '0098',
      'guild_id': '446075987680165888',
      'id': '450024877710245889',
      'level': 11,
      'message_count': 330,
      'username': 'timmy',
      'xp': 6607},


Get xp of a user
+++++++++++++++++++++++++++

Replace user_id with your user id.

.. code-block:: Python

    xp = await mee6API.levels.get_user_xp(user_id)
    print(xp)


Example of what it will return:

::

    42

Get the level of a user
+++++++++++++++++++++++++++

Replace user_id with your user id.

.. code-block:: Python

    level = await mee6API.levels.get_user_level(user_id)
    print(level)


Example of what it will return:

::

    5
