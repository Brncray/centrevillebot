import lightbulb
import hikari
import flare

plugin = lightbulb.Plugin('release', 'release')

bo = None


@plugin.command
@lightbulb.command('release', 'release session')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cmd(ctx):
    ...


def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")
