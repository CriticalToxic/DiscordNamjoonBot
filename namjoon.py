import discord,datetime
from discord.ext import commands


client = commands.Bot(command_prefix="bts!")

@client.event
async def on_ready():
    print("Namjoon is ready!")

@client.event
async def on_message(message):
    msg = message.content
    msg = msg.lower()

    if msg == "i love you joonie" or msg == "i love you namjoon":
        await message.channel.send("I love you {}".format(message.author.name))

    elif msg == "hi joonie" or msg == "hi namjoon" or msg == "hi daddy":
        await message.channel.send("Hello Kitten")

    elif msg == "hello joonie" or msg == "hello namjoon" or msg == "hello daddy":
        await message.channel.send("Hello Kitten")

    elif msg == "im screaming" or msg == "i am screaming" or msg == "i'm screaming":
        await message.channel.send("shut the fuck up, bitch!")

    elif msg == "hiya butt":
        await message.channel.send("alri lil mayyyy")

    await client.process_commands(message)
    txt = "[{}][{}]({}) {}: {}".format(datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"), message.guild.name, message.channel.name, message.author.name, message.content)
    f = open("chloelogs.txt","a")
    f.write(txt + "\n")
    f.close()
    print(txt)


@client.command(pass_context=True)
async def botinfo(ctx):
    embed=discord.Embed(title="Namjoon Bot", color=0x15cc55)
    embed.add_field(name="Prefix", value="bts!", inline=True)
    embed.add_field(name="Version", value="1.0.0", inline=True)
    embed.add_field(name="Author", value="Critical_Toxic", inline=True)

    await ctx.channel.send(embed=embed)
    


        



client.run("NzAyMjc2Nzg3MDAxODg0NzMx.Xp9s6A.iknbW4-5LChjw_iKEEOX2HnUJmw")
