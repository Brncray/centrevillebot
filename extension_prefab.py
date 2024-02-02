import lightbulb
import hikari


plugin = lightbulb.Plugin('', '')


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass


@plugin.command
@lightbulb.command('', '')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cmd(ctx):
    print("test command")



def load(bot):
    bot.add_plugin(plugin)
    print("Successfully loaded")
