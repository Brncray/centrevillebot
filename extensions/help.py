import lightbulb
import hikari


plugin = lightbulb.Plugin('', '')



@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass


@plugin.command
@lightbulb.command('cmdhelp', 'Get help on commands')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def host(ctx):
  response = (hikari.Embed(
    title="Help",
    color="#2a2d31"
  )
  .add_field(name="/profile", value="View your/other's profile. If a user has not had a ticket and has not registered a vehicle, they will not show up", inline=True)
  .add_field(name="/register", value="Register a vehicle" , inline=True)
             )
  await ctx.respond(response, flags=hikari.MessageFlag.EPHEMERAL)




def load(bot):
    bot.add_plugin(plugin)
    print("Successfully loaded")

def unload_session(bot):
    bot.remove_plugin(plugin)