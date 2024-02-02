import lightbulb
import hikari
import flare

plugin = lightbulb.Plugin('activity', 'activity')

bo = None


@plugin.command
@lightbulb.add_checks(
  lightbulb.has_roles(1184863530504163328)
)
@lightbulb.option('string', 'what string', type=str, required=True)
@lightbulb.command('activity', 'activity')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cmd(ctx):
  activity = hikari.Activity(name=ctx.options.string, type=hikari.ActivityType.WATCHING)
  await bo.update_presence(activity=activity)
  await ctx.respond('Updated', flags=hikari.MessageFlag.EPHEMERAL)


def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")


