#!/usr/bin/env python3

import dateutil.parser

from message_context import MessageContext
from models import GreedyStr


async def birthday(ctx: MessageContext, birthday: GreedyStr) -> None:
    """Remember a user's birthday so we can wish them a happy birthday later"""
    try:
        dateutil.parser.parse(birthday)
    except dateutil.parser.ParserError:
        await ctx.channel.send("I have no idea when that is. Try again.")
    else:
        ctx.server_ctx.add_birthday(ctx.discord_id, birthday)
        await ctx.channel.send("Okay, I'll remember your birthday for later!")
        # Need to reload since we've saved a birthday now
        ctx.server_ctx.reload()