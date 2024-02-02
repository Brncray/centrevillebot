import lightbulb
import hikari
import flare

plugin = lightbulb.Plugin('release', 'release')

bo = None


@flare.button(label="Session Link", style=hikari.ButtonStyle.PRIMARY)
async def release(
    ctx: flare.MessageContext,
    link: str
) -> None:
    await ctx.respond(content=link, flags=hikari.MessageFlag.EPHEMERAL)


@plugin.command
@lightbulb.add_checks(
  lightbulb.has_roles(1184863530504163328)
)
@lightbulb.option('link', 'link', type=str, required=True)
@lightbulb.option('frp', 'frp speeds', type=int, required=True)
@lightbulb.option('peacetime', 'peacetime', type=str, required=True)
@lightbulb.command('release', 'release session')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def releasecmd(ctx):
    try:
        await ctx.event.message.delete()
    except Exception:
        await ctx.respond('Sent', flags=hikari.MessageFlag.EPHEMERAL)
        pass
    row = await flare.Row(release(ctx.options.link))
    embed = hikari.Embed(
      title="Session Information", 
      description=f"Peacetime: **{ctx.options.peacetime}**\nFRP Speeds: **{ctx.options.frp}**\n\nKick = Infraction\n\nRead all server information before joining, all rules are strictly enforced.",
      color="#2a2d31"
      
    )
    await bo.rest.create_message(ctx.channel_id, "@everyone",embed=embed, component=row, mentions_everyone=True)


def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")
