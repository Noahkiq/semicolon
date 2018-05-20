from discord.ext import commands
import subprocess
import random


bot = commands.Bot(command_prefix=[';', 'semicolon '])


def longMessage(message):
    """Use this to prevent the bot from trying to send messages over 2000 characters."""
    if len(message) > 2000:
        return "hey!! you tricked me into making a big message!! no fair :(("
    else:
        return message


def formatSentence(variableList, finalSeparator="and"):
    """Turn a list of variables into a string, like 'Bill, John, and Jeff.'"""
    # Thanks to StackOverflow user Shashank: https://stackoverflow.com/a/30084397
    n = len(variableList)  # Creates a variable for the number of objects being formatted
    if n > 1:
        return ('{}, '*(n-2) + '{} Q*Q*Q {}').format(*variableList).replace("Q*Q*Q", finalSeparator)  # shut up
    elif n > 0:
        return variableList[0]  # If only one string was input, it gets returned.
    else:
        return ''  # If user entered no input, return nothing.


def cowsayHelper(cowcmd, author, arguments):
    """cowsay helper function"""
    command = [cowcmd]
    command += arguments.replace('-f head-in', '').split()
    output = subprocess.check_output(command).decode("utf-8")
    return longMessage(f"here you go {author.mention} :D ```{output}```")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(aliases=['say', 'repeat'])
async def echo(ctx, *, text):
    """Have the bot repeat what you say."""
    output = longMessage(text.replace('@', '@​'))
    await ctx.send(output)


@bot.command(aliases=['r'])
async def reverse(ctx, *, text):
    """Reverse your text.txet ruoy esreveR"""
    output = longMessage(text[::-1].replace('@', '@​'))
    await ctx.send(output)


@bot.command(aliases=['cow'])
async def cowsay(ctx, *, text):
    """Spice up your funny quotes and memes with a talking cow!"""
    try:
        await ctx.send(cowsayHelper("cowsay", ctx.author, text))
    except:
        await ctx.send("oi. i dunno what you just tried to do but you broke the command. don't do that again >:(")


@bot.command()
async def cowthink(ctx, *, text):
    """It's like cowsay, but the cow's thinking."""
    try:
        await ctx.send(cowsayHelper("cowthink", ctx.author, text))
    except:
        await ctx.send("oi. i dunno what you just tried to do but you broke the command. don't do that again >:(")


@bot.command(aliases=['cookie'])
async def fortune(ctx):
    """Crack open a virtual cookie."""
    output = subprocess.check_output("fortune").decode("utf-8").replace("\n", "")
    await ctx.send(f"Today's cookie says... *{output}*")


@bot.command(aliases=['cookiecow'])
async def fortunecow(ctx):
    """Crack open a virtual cookie. Then feed it to a cow."""
    output = subprocess.check_output("fortune | cowsay", shell=True).decode("utf-8")
    await ctx.send(f"```{output}```")


@bot.command(aliases=['diceroll', 'rolldice'])
async def roll(ctx, sides=6, dice=1):
    """Roll a die! Or multiple dice with different sides!"""
    if sides < 1 or dice < 1:
        await ctx.send("Please use numbers greater than zero :heart:")
        return  # exit the command
    if len(f'{sides*dice}') > 1000 or len(f'{sides}') > 25 or dice > 100:
        await ctx.send("These numbers look kinda big...")
        return

    diceRolled = 0
    diceOutput = []
    while diceRolled < dice:
        diceRolled += 1
        diceOutput.append(random.randint(1, sides))

    numbers = formatSentence(diceOutput, "and a")
    output = longMessage(f"I rolled a {numbers}! :D")
    await ctx.send(output)


bot.run(open("token.txt").read().split("\n")[0])
