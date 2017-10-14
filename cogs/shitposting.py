import hashlib
import random

import discord
from discord.ext import commands

class ShitPosting:
    @commands.command()
    async def clap(self, ctx: commands.Context, *, msg):
        """
        :clap: your :clap: message :clap: here :clap:
        """
        msg = await commands.clean_content().convert(ctx, msg)
        await ctx.send(content="\n".join([":clap: " + " :clap: ".join(line.split(" ")) + " :clap:"
                                          for line in msg.split('\n')]))

    @commands.command()
    async def owo(self, ctx: commands.Context, *, msg):
        """
        Say something in a 'cute' way
        """
        msg = await commands.clean_content().convert(ctx, msg)
        transforms = {'na': 'nya',
                      'ne': 'nye',
                      'ni': 'nyi',
                      'nu': 'nyu',
                      'no': 'nyo',
                      'r': 'w',
                      'l': 'w'}
        for src, dst in transforms.items():
            msg = msg.replace(src, dst).replace(src.upper(), dst.upper()).replace(src.title(), dst.title())
        await ctx.send(content=msg)

    @commands.command(aliases=['leet'])
    async def l33t(self, ctx: commands.Context, *, msg):
        """
        L33t m3ss4g1ng
        """
        msg = await commands.clean_content().convert(ctx, msg)
        transforms = {'e': '3',
                      'i': '1',
                      'o': '0',
                      'a': '4',
                      's': '5',
                      'v': '\\\\/',
                      'n': '|\\\\|'}
        for src, dst in transforms.items():
            msg = msg.replace(src.lower(), dst)
        await ctx.send(content=msg)