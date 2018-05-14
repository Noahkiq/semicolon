from discord.ext import commands
import subprocess
import time
import re


bot = commands.Bot(command_prefix=[';', 'semicolon '])
badarg = re.compile(r"-\w")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(aliases=['say', 'repeat'])
async def echo(ctx, *, text):
    """Have the bot repeat what you say."""
    await ctx.send(text)


@bot.command(aliases=['r'])
async def reverse(ctx, *, text):
    """Reverse your text.txet ruoy esreveR"""
    await ctx.send(text[::-1])


@bot.command(aliases=['cow', 'csay'])
async def cowsay(ctx, *, text):
    """Spice up your funny quotes and memes with a talking cow!"""
    try:
        args = text.split()
        args[0] = badarg.sub("...", args[0])
        output = subprocess.check_output(["/usr/bin/cowsay", " ".join(args).replace("head-in", "default")])
        output = output.decode("utf-8")
        await ctx.send(f"here you go {ctx.author.mention} senpai~ ❤ ```{output}```")
    except TimeoutError as e:
        await ctx.send("an error occurred while running the command")
        ltime = time.localtime(time.time())
        timestring = f'{ltime.tm_year}-{ltime.tm_mon}-{ltime.tm_mday} {ltime.tm_hour}:{ltime.tm_min}'
        with open('errors.txt', 'a') as logfile:
            logfile.write(f'[{timestring}] {e}\n')


@bot.command(aliases=['cookie'])
async def fortune(ctx):
    """Crack open a virtual cookie."""
    output = subprocess.check_output("fortune", shell=True).decode("utf-8").replace("\n", "")
    await ctx.send(f"Today's cookie says... *{output}*")


@bot.command(aliases=['cookiecow'])
async def fortunecow(ctx):
    """Crack open a virtual cookie. Then feed it to a cow."""
    output = subprocess.check_output("fortune | cowsay", shell=True).decode("utf-8")
    await ctx.send(f"```{output}```")

bot.run(open("token.txt").read().split("\n")[0])
