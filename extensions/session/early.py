import lightbulb
import hikari
import flare

plugin = lightbulb.Plugin('early', 'early')

bo = None


@plugin.command
@lightbulb.add_checks(
  lightbulb.has_roles(1184863530504163328)
)
@lightbulb.command('early', 'early')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cmd(ctx):
    try:
        await ctx.event.message.delete()
    except Exception:
        await ctx.respond('Sent', flags=hikari.MessageFlag.EPHEMERAL)
        pass
    await bo.rest.create_message(ctx.channel_id, f"**Centreville Early Access:**\n- Private message <@{ctx.author.id}> for the link to the session. Please be reminded that not everyone will be able to join the server. @everyone \n\n__Pre-Release Limit:__ \n6 Law Enforcement \n2 Greenville Fire Department \n4 Platinum Members", mentions_everyone=True)


def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")


