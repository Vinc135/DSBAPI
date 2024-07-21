import discord
import datetime

def limit_characters(string: str, limit: int):
    if len(string) > limit:
        return string[:limit-3] + "..."
    return string

async def send_error(title, description, interaction):
    embed = discord.Embed(colour=discord.Colour.red(), title=title, description=description)
    embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
    embed.set_footer(text="Premium jetzt veröffentlicht! www.vulpo-bot.de/premium")
    try:
        await interaction.response.send_message(embed=embed, ephemeral=True)
    except:
        try:
            await interaction.response.send_message("**<:v_kreuz:1049388811353858069> Mir fehlt die Berechtigung 'Nachrichten einbetten'.**", ephemeral=True)
        except:
            pass