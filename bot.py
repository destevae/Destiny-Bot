# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='//')


# Main currency conversion system
@bot.command(name='convert', help='Convert Karuta currency.')
async def convert(ctx, quantity: int, type_of_item: str):
    if ctx.author == bot.user:
        return

    # Variables
    spacedStr = " " + type_of_item
    desc = str(quantity) + spacedStr

    # Converting gems
    if type_of_item == 'gems' or type_of_item == 'gem':
        goldLow = round(quantity * 36.67, 1)
        goldHigh = round(quantity * 30, 1)
        ticketConvert = round(quantity / 15, 1)
        dropletConvert = round(quantity / 33, 1)

        # Embed
        embed = discord.Embed(title="Karuta Bot Conversions",
                              url="https://a.com/",
                              description="Rates for: " + desc,
                              color=discord.Color.blue())

        embed.add_field(name="Gold 💰", value=str(goldLow) + "-" +
                        str(goldHigh) + " gold", inline=False)
        embed.add_field(name="Tickets 🎟️", value=str(ticketConvert) +
                        " tickets", inline=False)
        embed.add_field(name="Droplets 💧", value=str(dropletConvert) +
                        " droplets", inline=False)

    # Converting tickets
    if type_of_item == 'tickets' or type_of_item == 'ticket':
        goldLow = round(quantity * 500, 1)
        goldHigh = round(quantity * 600, 1)
        gemConvert = round(quantity * 15, 1)
        dropletConvert = round(quantity / 2.2, 1)

        # Embed
        embed = discord.Embed(title="Karuta Bot Conversions",
                              url="https://a.com/",
                              description="Rates for: " + desc,
                              color=discord.Color.red())

        embed.add_field(name="Gold 💰", value=str(goldLow) + "-" +
                        str(goldHigh) + " gold", inline=False)
        embed.add_field(name="Gems 💎", value=str(gemConvert) +
                        " gems", inline=False)
        embed.add_field(name="Droplets 💧", value=str(dropletConvert) +
                        " droplets", inline=False)

    # Converting gold
    if type_of_item == 'gold':
        gemLow = round(quantity / 36.67, 1)
        gemHigh = round(quantity / 30, 1)
        ticketLow = round(quantity / 600, 1)
        ticketHigh = round(quantity / 500, 1)
        dropletLow = round(quantity / 1300, 1)
        dropletHigh = round(quantity / 1000, 1)

        # Embed
        embed = discord.Embed(title="Karuta Bot Conversions",
                              url="https://a.com/",
                              description="Rates for: " + desc,
                              color=discord.Color.gold())

        embed.add_field(name="Gems 💎", value=str(gemLow) + "-" +
                        str(gemHigh) + " gems", inline=False)
        embed.add_field(name="Tickets 🎟️", value=str(ticketLow) + "-" +
                        str(ticketHigh) + " tickets", inline=False)
        embed.add_field(name="Droplets 💧 (Not so accurate)",
                        value=str(dropletLow) + "-" + str(dropletHigh) +
                        " droplets", inline=False)

    # Converting droplets
    if type_of_item == 'droplets' or type_of_item == 'droplet':
        goldLow = round(quantity * 1000, 1)
        goldHigh = round(quantity * 1300, 1)
        gemConvert = round(quantity * 33, 1)
        ticketConvert = round(quantity * 2.2, 1)

        # Embed
        embed = discord.Embed(title="Karuta Bot Conversions",
                              url="https://a.com/",
                              description="Rates for: " + desc,
                              color=discord.Color.dark_blue())

        embed.add_field(name="Gold 💰 (Not so accurate)", value=str(goldLow) +
                        "-" + str(goldHigh) + " gold", inline=False)
        embed.add_field(name="Gems 💎", value=str(gemConvert) +
                        " gems", inline=False)
        embed.add_field(name="Tickets 🎟️", value=str(ticketConvert) +
                        " tickets", inline=False)

    await ctx.send(embed=embed)


# Rates function
@bot.command()
async def rates(ctx):

    # Pages
    page1 = discord.Embed(
        title='Gems',
        description='Trading rates for gems',
        colour=discord.Colour.blue()
    )
    page2 = discord.Embed(
        title='Tickets',
        description='Trading rates for tickets',
        colour=discord.Colour.red()
    )
    page3 = discord.Embed(
        title='Gold',
        description='Trading rates for gold',
        colour=discord.Colour.gold()
    )
    page4 = discord.Embed(
        title='Droplets',
        description='Trading rates for droplets',
        colour=discord.Colour.dark_blue()
    )

    # Fields
    page1.add_field(name="Gems to Tickets Rate", value='15 💎 : 1 🎟️',
                    inline=False)
    page1.add_field(name="Gems to Gold Rate", value='1 💎 : 30-30.67 💰',
                    inline=False)
    page1.add_field(name="Gems to Droplets Rate", value='33 💎 : 1 💧',
                    inline=False)

    page2.add_field(name="Tickets to Gems Rate", value='1 🎟️ : 15 💎',
                    inline=False)
    page2.add_field(name="Tickets to Gold Rate", value='1 🎟️ : 500-600 💰',
                    inline=False)
    page2.add_field(name="Tickets to Droplets Rate", value='2.2 🎟️ : 1 💧',
                    inline=False)

    page3.add_field(name="Gold to Tickets Rate", value='500-600 💰 : 1 🎟️',
                    inline=False)
    page3.add_field(name="Gold to Gems Rate", value='30-30.67 💰 : 1 💎',
                    inline=False)
    page3.add_field(name="Gold to Droplets Rate", value='1000-1300 💰 : 1 💧 (Not accurate!)',
                    inline=False)

    page4.add_field(name="Droplets to Gems Rate", value='1 💧 : 33 💎',
                    inline=False)
    page4.add_field(name="Droplets to Tickets Rate", value='1 💧 : 2.2 🎟️',
                    inline=False)
    page4.add_field(name="Droplets to Gold Rate", value='1 💧 : 1000-1300 💰 (Not accurate!)',
                    inline=False)

    pages = [page1, page2, page3, page4]

    message = await ctx.send(embed=page1)
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('⏭')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed=pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            if i < 3:
                i += 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '⏭':
            i = 3
            await message.edit(embed=pages[i])

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0,
                                                check=check)
            await message.remove_reaction(reaction, user)

        except:
            break

    await message.clear_reactions()


# Stop Destiny Bot
@bot.command(name='stop', help='Just for desteva to stop the bot running :)')
async def stop(ctx):
    if ctx.author == bot.user:
        return
    msg = 'Bot successfully stopped :)'
    await ctx.send(msg)
    await bot.close()


# Custom Discord status, purely for aesthetics
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Karuta conversion...'))


# Invite Destiny Bot
@bot.command(name='invite', description='Create an invite link')
async def invite(ctx):
    embed = discord.Embed(title="Invite the bot!",
                          description="https://discord.com/api/oauth2/authorize?client_id=731625637160157214&permissions=8&scope=bot",
                          color=discord.Color.blue())
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/697970014476828686/1062906322544238592/Destiny-Bot-PFP.png")

    await ctx.send(embed=embed)

bot.run(TOKEN)
