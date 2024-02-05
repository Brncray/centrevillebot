import lightbulb
import hikari
import flare

plugin = lightbulb.Plugin('reinvites', 'do reinvites')

bo = None


@flare.button(label="Session Link", style=hikari.ButtonStyle.PRIMARY)
async def reinvites(
        ctx: flare.MessageContext,
        link: str
) -> None:
    await ctx.respond(content=link, flags=hikari.MessageFlag.EPHEMERAL)


@plugin.command
@lightbulb.add_checks(
    lightbulb.has_roles(1184863530504163328)
)
@lightbulb.option('link', 'link', type=str, required=True)
@lightbulb.option('peacetime', 'peacetime', type=str, required=True)
@lightbulb.command('reinvites', 'do reinvites')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def releasecmd(ctx):
    try:
        await ctx.event.message.delete()
    except Exception:
        await ctx.respond('Sent', flags=hikari.MessageFlag.EPHEMERAL)
        pass
    pt = None
    frp = None
    row = await flare.Row(reinvites(ctx.options.link))

    if ctx.options.peacetime.lower() == "normal":
        pt = "Normal"
        frp = "80"
    elif ctx.options.peacetime.lower() == "strict":
        pt = "Strict"
        frp = "70"
    else:
        await ctx.respond('Please use a valid peacetime', flags=hikari.MessageFlag.EPHEMERAL)
        return
    embed = hikari.Embed(
        title="Re-Invites",
        description=f"Peacetime: **{pt}**\nFRP Speeds: **{frp}**\n\nKick = Infraction\n\nRead all server information before joining, all rules are strictly enforced.",
        color="#2a2d31"

    )
    await bo.rest.create_message(ctx.channel_id, "@here", embed=embed, component=row, mentions_everyone=True)


def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")
