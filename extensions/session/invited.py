import lightbulb
import hikari
import flare

plugin = lightbulb.Plugin('invited', 'invited')

bo = None


@plugin.command
@lightbulb.add_checks(
  lightbulb.has_roles(1184863530504163328)
)
@lightbulb.command('invited', 'invited')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cmd(ctx):
    try:
        await ctx.event.message.delete()
    except Exception:
        await ctx.respond('Sent', flags=hikari.MessageFlag.EPHEMERAL)
        pass
    await bo.rest.create_message(ctx.channel_id, f"Early access for <@{ctx.author.id}>’s session has now been concluded. The links have been issued to all of the members who messaged this host conscious of the limits.")


def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")


