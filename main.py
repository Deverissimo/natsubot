from datetime import datetime
import idol_info
import discord
from discord.ext import commands
import os
import dotenv

# Set this to the prefix you want for your bot.
prefix = "$"
client = commands.Bot(command_prefix=prefix)
client.remove_command("help")


# for when the bot comes online
@client.event
async def on_ready():
    print("Natsubot is now online!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #School Idol Project character information embed
    

    if message.content.startswith(prefix + 'honoka'):
        embed_var = discord.Embed(title=idol_info.idol[0][0],
                                  description="**Seiyuu**: Nitta Emi",
                                  color=0xf39801,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[1], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][0],
                            inline=True)
        embed_var.add_field(name="Birthday", value="September 12")
        embed_var.add_field(name="Hex Color", value="#f39801")
        embed_var.set_author(name="About Honoka", icon_url=idol_info.honoka[0])
        embed_var.set_thumbnail(url=idol_info.honoka[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'kotori'):
        embed_var = discord.Embed(title=idol_info.idol[0][1],
                                  description="**Seiyuu**: Uchida Aya",
                                  color=0xabadac,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[1], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][0],
                            inline=True)
        embed_var.add_field(name="Birthday", value="September 12")
        embed_var.add_field(name="Hex Color", value="#abadac")
        embed_var.set_author(name="About Kotori", icon_url=idol_info.kotori[0])
        embed_var.set_thumbnail(url=idol_info.kotori[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'umi'):
        embed_var = discord.Embed(title=idol_info.idol[0][2],
                                  description="**Seiyuu**: Mimori Suzuko",
                                  color=0x2c72b7,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[1], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="March 15")
        embed_var.add_field(name="Hex Color", value="#2c72b7")
        embed_var.set_author(name="About Umi", icon_url=idol_info.umi[0])
        embed_var.set_thumbnail(url=idol_info.umi[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'rin'):
        embed_var = discord.Embed(title=idol_info.idol[0][3],
                                  description="**Seiyuu**: Iida Riho",
                                  color=0xfef102,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="November 1")
        embed_var.add_field(name="Hex Color", value="fef102")
        embed_var.set_author(name="About Rin", icon_url=idol_info.rin[0])
        embed_var.set_thumbnail(url=idol_info.rin[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'hanayo'):
        embed_var = discord.Embed(title=idol_info.idol[0][4],
                                  description="**Seiyuu**: Kubo Yurika",
                                  color=0x23ac3a,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][0],
                            inline=True)
        embed_var.add_field(name="Birthday", value="January 17")
        embed_var.add_field(name="Hex Color", value="23ac3a")
        embed_var.set_author(name="About Hanayo", icon_url=idol_info.hanayo[0])
        embed_var.set_thumbnail(url=idol_info.hanayo[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'maki'):
        embed_var = discord.Embed(title=idol_info.idol[0][5],
                                  description="**Seiyuu**: Hori Eriko",
                                  color=0xe93421,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][2],
                            inline=True)
        embed_var.add_field(name="Birthday", value="April 19")
        embed_var.add_field(name="Hex Color", value="e93421")
        embed_var.set_author(name="About Maki", icon_url=idol_info.maki[0])
        embed_var.set_thumbnail(url=idol_info.maki[1])
        await message.channel.send(embed=embed_var)


    if message.content.startswith(prefix + 'nozomi'):
        embed_var = discord.Embed(title=idol_info.idol[0][6],
                                  description="**Seiyuu**: Kusuda Aina",
                                  color=0x925da3,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value='June 9')
        embed_var.add_field(name="Hex Color", value='925da3')
        embed_var.set_author(name="About Nozomi", icon_url=idol_info.nozomi[0])
        embed_var.set_thumbnail(url=idol_info.nozomi[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'nico'):
        embed_var = discord.Embed(title=idol_info.idol[0][7],
                                  description="**Seiyuu**: Tokui Sora",
                                  color=0xec6f9b,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="July 22")
        embed_var.add_field(name="Hex Color", value="ec6f9b")
        embed_var.set_author(name="About Nico", icon_url=idol_info.nico[0])
        embed_var.set_thumbnail(url=idol_info.nico[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'eli'):
        embed_var = discord.Embed(title=idol_info.idol[0][8],
                                  description="**Seiyuu**: Nanjou Yoshino",
                                  color=0x1eb8ec,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="October 21")
        embed_var.add_field(name="Hex Color", value="1eb8ec")
        embed_var.set_author(name="About Eli", icon_url=idol_info.eli[0])
        embed_var.set_thumbnail(url=idol_info.eli[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'chika'):
        embed_var = discord.Embed(title=idol_info.idol[1][0],
                                  description="**Seiyuu**: Inami Anju",
                                  color=0xf28100,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[1],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[1], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[1], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[1][0],
                            inline=True)
        embed_var.add_field(name="Birthday", value="August 1")
        embed_var.add_field(name="Hex Color", value="f28100")
        embed_var.set_author(name="About Chika", icon_url=idol_info.chika[0])
        embed_var.set_thumbnail(url=idol_info.chika[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'riko'):
        embed_var = discord.Embed(title=idol_info.idol[1][1],
                                  description="**Seiyuu**: Aida Rikako",
                                  color=0xf39c95,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[1],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[1], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[1], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[1][2],
                            inline=True)
        embed_var.add_field(name="Birthday", value="September 19")
        embed_var.add_field(name="Hex Color", value="f39c95")
        embed_var.set_author(name="About Riko", icon_url=idol_info.riko[0])
        embed_var.set_thumbnail(url=idol_info.riko[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'you'):
        embed_var = discord.Embed(title=idol_info.idol[1][2],
                                  description="**Seiyuu**: Saitou Shuka",
                                  color=0x67aadf,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[1],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[1], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[1], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[1][0],
                            inline=True)
        embed_var.add_field(name="Birthday", value="April 17")
        embed_var.add_field(name="Hex Color", value="67aadf")
        embed_var.set_author(name="About You (I mean the character)",
                             icon_url=idol_info.you[0])
        embed_var.set_thumbnail(url=idol_info.you[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(
            prefix + 'hanamaru') or message.content.startswith(prefix +
                                                               'zura'):
        embed_var = discord.Embed(title=idol_info.idol[1][3],
                                  description='**Seiyuu**: Takatsuki Kanako',
                                  color=0xfee202,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[1],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[1], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[1][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="March 4")
        embed_var.add_field(name="Hex Color", value="fee202")
        embed_var.set_author(name="About Hanamaru",
                             icon_url=idol_info.hanamaru[0])
        embed_var.set_thumbnail(url=idol_info.hanamaru[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'ruby'):
        embed_var = discord.Embed(title=idol_info.idol[1][4],
                                  description="**Seiyuu**: Furihata Ai",
                                  color=0xee6da6,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[1],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[1], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[1][0],
                            inline=True)
        embed_var.add_field(name="Birthday", value="September 21")
        embed_var.add_field(name="Hex Color", value="ee6da6")
        embed_var.set_author(name="About Ruby", icon_url=idol_info.ruby[0])
        embed_var.set_thumbnail(url=idol_info.ruby[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(
            prefix + 'yoshiko') or message.content.startswith(prefix +
                                                              'yohane'):
        embed_var = discord.Embed(title=idol_info.idol[1][5],
                                  description="**Seiyuu**: Kobayashi Aika",
                                  color=0x9f9f9f,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[1],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[1], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[1][2],
                            inline=True)
        embed_var.add_field(name="Birthday", value="July 13")
        embed_var.add_field(name="Hex Color", value="9f9f9f")
        embed_var.set_author(name="About Yoshiko",
                             icon_url=idol_info.yoshiko[0])
        embed_var.set_thumbnail(url=idol_info.yoshiko[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'dia'):
        embed_var = discord.Embed(title=idol_info.idol[1][6],
                                  description="**Seiyuu**: Komiya Arisa",
                                  color=0xe70014,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[1],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[2], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[1], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[1][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="January 1")
        embed_var.add_field(name="Hex Color", value="e70014")
        embed_var.set_author(name="About ", icon_url=idol_info.dia[0])
        embed_var.set_thumbnail(url=idol_info.dia[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'mari'):
        embed_var = discord.Embed(title=idol_info.idol[1][7],
                                  description="**Seiyuu**: Suzuki Aina",
                                  color=0x6458a4,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[1],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[2], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[1], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[1][2],
                            inline=True)
        embed_var.add_field(name="Birthday", value="June 13")
        embed_var.add_field(name="Hex Color", value="6458a4")
        embed_var.set_author(name="About ", icon_url=idol_info.mari[0])
        embed_var.set_thumbnail(url=idol_info.mari[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'kanan'):
        embed_var = discord.Embed(title=idol_info.idol[1][8],
                                  description="**Seiyuu**: Suwa Nanaka",
                                  color=0x63c0ad,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[1],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[2], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[1], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[1][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="February 10")
        embed_var.add_field(name="Hex Color", value="63c0ad")
        embed_var.set_author(name="About ", icon_url=idol_info.kanan[0])
        embed_var.set_thumbnail(url=idol_info.kanan[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'ayumu'):
        embed_var = discord.Embed(title=idol_info.idol[2][0],
                                  description="**Seiyuu**: Oonishi Aguri",
                                  color=0xf0939e,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[2],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[1], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[2], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[2][0],
                            inline=True)
        embed_var.add_field(name="Birthday", value="March 1")
        embed_var.add_field(name="Hex Color", value="f0939e")
        embed_var.set_author(name="About ", icon_url=idol_info.ayumu[0])
        embed_var.set_thumbnail(url=idol_info.ayumu[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'setsuna'):
        embed_var = discord.Embed(title=idol_info.idol[2][1],
                                  description="**Seiyuu**: Kusunoki Tomori",
                                  color=0xda363f,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[2],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[1], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[2], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[2][0],
                            inline=True)
        embed_var.add_field(name="Birthday", value="August 8")
        embed_var.add_field(name="Hex Color", value="da363f")
        embed_var.set_author(name="About ", icon_url=idol_info.setsuna[0])
        embed_var.set_thumbnail(url=idol_info.setsuna[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'lanzhu'):
        embed_var = discord.Embed(title=idol_info.idol[2][2],
                                  description="**Seiyuu**: Homoto Akina",
                                  color=0xefc3c0,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[2],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[1], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[2], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[2][3],
                            inline=True)
        embed_var.add_field(name="Birthday", value="February 15")
        embed_var.add_field(name="Hex Color", value="efc3c0")
        embed_var.set_author(name="About Lanzhu", icon_url=idol_info.lanzhu[0])
        embed_var.set_thumbnail(url=idol_info.lanzhu[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'ai'):
        embed_var = discord.Embed(title=idol_info.idol[2][3],
                                  description="**Seiyuu**: Murakami Natsumi",
                                  color=0xeb6001,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[2],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[1], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[2], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[2][2],
                            inline=True)
        embed_var.add_field(name="Birthday", value="May 30")
        embed_var.add_field(name="Hex Color", value="eb6001")
        embed_var.set_author(name="About Ai", icon_url=idol_info.ai[0])
        embed_var.set_thumbnail(url=idol_info.ai[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'shioriko'):
        embed_var = discord.Embed(title=idol_info.idol[2][4],
                                  description="**Seiyuu**: Koizumi Moeka",
                                  color=0x2c9e7e,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[2],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[2], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[2][3],
                            inline=True)
        embed_var.add_field(name="Birthday", value="October 5")
        embed_var.add_field(name="Hex Color", value="2c9e7e")
        embed_var.set_author(name="About shioriko",
                             icon_url=idol_info.shioriko[0])
        embed_var.set_thumbnail(url=idol_info.shioriko[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'shizuku'):
        embed_var = discord.Embed(title=idol_info.idol[0][0],
                                  description="**Seiyuu**: Maeda Kaori",
                                  color=0x81c6ef,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[2],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[2], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[2][0],
                            inline=True)
        embed_var.add_field(name="Birthday", value="April 3")
        embed_var.add_field(name="Hex Color", value="81c6ef")
        embed_var.set_author(name="About Shizuku",
                             icon_url=idol_info.shizuku[0])
        embed_var.set_thumbnail(url=idol_info.shizuku[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'rina'):
        embed_var = discord.Embed(title=idol_info.idol[0][0],
                                  description="**Seiyuu**: Tanaka Chiemi",
                                  color=0xa8aaa9,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[2],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[2], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[2][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="November 13")
        embed_var.add_field(name="Hex Color", value="a8aaa9")
        embed_var.set_author(name="About ", icon_url=idol_info.rina[0])
        embed_var.set_thumbnail(url=idol_info.rina[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'kasumi'):
        embed_var = discord.Embed(title=idol_info.idol[0][0],
                                  description="**Seiyuu**: Sagara Mayu",
                                  color=0xf7f064,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[2],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[2], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[2][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="January 23")
        embed_var.add_field(name="Hex Color", value="f7f064")
        embed_var.set_author(name="About ", icon_url=idol_info.kasumi[0])
        embed_var.set_thumbnail(url=idol_info.kasumi[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'karin'):
        embed_var = discord.Embed(title=idol_info.idol[0][0],
                                  description="**Seiyuu**: Kubota Miyu",
                                  color=0x034099,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[2],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[2], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[2], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[2][2],
                            inline=True)
        embed_var.add_field(name="Birthday", value="June 29")
        embed_var.add_field(name="Hex Color", value="034099")
        embed_var.set_author(name="About ", icon_url=idol_info.karin[0])
        embed_var.set_thumbnail(url=idol_info.karin[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'emma'):
        embed_var = discord.Embed(title=idol_info.idol[0][0],
                                  description="**Seiyuu**: Nitta Emi",
                                  color=0xabadac,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="emma")
        embed_var.add_field(name="Hex Color", value="emma")
        embed_var.set_author(name="About ", icon_url=idol_info.emma[0])
        embed_var.set_thumbnail(url=idol_info.emma[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'kanata'):
        embed_var = discord.Embed(title=idol_info.idol[0][0],
                                  description="**Seiyuu**: Nitta Emi",
                                  color=0xabadac,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="kanata")
        embed_var.add_field(name="Hex Color", value="kanata")
        embed_var.set_author(name="About ", icon_url=idol_info.kanata[0])
        embed_var.set_thumbnail(url=idol_info.kanata[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'mia'):
        embed_var = discord.Embed(title=idol_info.idol[0][0],
                                  description="**Seiyuu**: Nitta Emi",
                                  color=0xabadac,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="mia")
        embed_var.add_field(name="Hex Color", value="mia")
        embed_var.set_author(name="About ", icon_url=idol_info.mia[0])
        embed_var.set_thumbnail(url=idol_info.mia[1])
        await message.channel.send(embed=embed_var)

    if message.content.startswith(prefix + 'yu'):
        embed_var = discord.Embed(title=idol_info.idol[0][0],
                                  description="**Seiyuu**: Nitta Emi",
                                  color=0xabadac,
                                  timestamp=datetime.utcnow())
        embed_var.add_field(name="School",
                            value=idol_info.school[0],
                            inline=True)
        embed_var.add_field(name="Year", value=idol_info.year[0], inline=True)
        embed_var.add_field(name="Group", value=idol_info.unit[0], inline=True)
        embed_var.add_field(name="Sub Unit",
                            value=idol_info.sub_unit[0][1],
                            inline=True)
        embed_var.add_field(name="Birthday", value="yu")
        embed_var.add_field(name="Hex Color", value="yu")
        embed_var.set_author(name="About ", icon_url=idol_info.yu[0])
        embed_var.set_thumbnail(url=idol_info.yu[1])
        await message.channel.send(embed=embed_var)

dotenv.load_dotenv()
client.run(os.environ.get("bot_token"))
