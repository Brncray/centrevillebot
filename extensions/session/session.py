import lightbulb
import hikari


plugin = lightbulb.Plugin('session', 'Host a session')



@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass


@plugin.command
@lightbulb.add_checks(
  lightbulb.has_roles(1184863530504163328)
)
@lightbulb.option("reactions", "How many reactions are required", type=int, required=True)
@lightbulb.command('session', 'Host a session')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def host(ctx):
    try:
        await ctx.event.message.delete()
    except Exception:
        pass

    author = ctx.author.id
    channel = ctx.channel_id
    embed = None

    embed = (hikari.Embed
    (
        title="Centreville Server Startup!",
        description=f"<@{author}> is hosting a session! {ctx.options.reactions}+ reactions are required for this session to commence.",
        color="#2a2d31"
    ))



    message = await ctx.respond("@everyone", embed=embed, mentions_everyone=False)
    msg = await message.message()
    await msg.add_reaction(":Thumbup1:1153703169545752607")





def load(bot):
    bot.add_plugin(plugin)
    print("Successfully loaded")

def unload_session(bot):
    bot.remove_plugin(plugin)