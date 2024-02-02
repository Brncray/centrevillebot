import lightbulb
import hikari
import flare

plugin = lightbulb.Plugin('setting', 'setting up')

bo = None


@plugin.command
@lightbulb.command('setting', 'setting up')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cmd(ctx):
    try:
        await ctx.event.message.delete()
    except Exception:
        await ctx.respond('Sent', flags=hikari.MessageFlag.EPHEMERAL)
        pass
    await bo.rest.create_message(ctx.channel_id, "The host is now setting up. Early access please refer to the designated early access channel.")


def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")
