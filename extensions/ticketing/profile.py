import lightbulb
import hikari
import flare
from pymongo import MongoClient

plugin = lightbulb.Plugin('', '')

bo = None
client = MongoClient("mongodb+srv://brncray:Bobrien@bot.lvf7vud.mongodb.net/?retryWrites=true&w=majority")

@flare.button(label="Registered Vehicles", style=hikari.ButtonStyle.PRIMARY)
async def registered(
    ctx: flare.MessageContext,
    user_id: int
) -> None:

    db = client.get_database('data')
    records = db.ticketing
    resp = records.find_one({'user_id': user_id})
    arr = resp.get("vehicles", [])
    string = ""
    labels = [
        'Model:',
        'License Plate:',
        'Color:'
    ]
    for outer_array in arr:
        for element_index, inner_array in enumerate(outer_array):
            if element_index == 0:
                inner_array = f"**{inner_array}**"
            if element_index == 2:
                inner_array = f"{inner_array}\n-----------"

            label = labels[element_index]
            string = string + f"\n{label} {inner_array}"
    response = (hikari.Embed(
        title=f"Registered Vehicles",
        description=f"{string}",
        color="#2a2d31"
    ).set_footer(text="Centreville Roleplay", icon=bo.get_me().avatar_url)
    )
    await ctx.respond(response, flags=hikari.MessageFlag.EPHEMERAL)

@flare.button(label="Citations", style=hikari.ButtonStyle.PRIMARY)
async def citations(
    ctx: flare.MessageContext,
    user_id: int
) -> None:

    db = client.get_database('data')
    records = db.ticketing
    resp = records.find_one({'user_id': user_id})
    arr = resp.get("citations", [])
    string = ""
    labels = [
        '**Charges:**',
        'Officer:',
        'Department:',
        'Amount:'
    ]

    for outer_array in arr:
        for element_index, inner_array in enumerate(outer_array):
            if element_index == 0:
                inner_array = f"**{inner_array}**"
            if element_index == 3:
                inner_array = f"{inner_array}\n-----------------------------------"
            label = labels[element_index]
            string = string + f"\n{label} {inner_array}"
    response = (hikari.Embed(
        title=f"Citations",
        description=f"{string}",
        color="#2a2d31"
    ).set_footer(text="Centreville Roleplay", icon=bo.get_me().avatar_url)
    )
    await ctx.respond(response, flags=hikari.MessageFlag.EPHEMERAL)

@plugin.command
@lightbulb.option('user', 'what user', type=hikari.Member, required=False)
@lightbulb.command('profile', 'look at your profile', auto_defer=True)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cmd(ctx):
    db = client.get_database('data')
    license = None
    records = db.ticketing
    try:
        await ctx.event.message.delete()
    except Exception:
        pass
    if ctx.options.user is None:
        user = ctx.author
    elif ctx.options is not None:
        user = ctx.options.user

    resp = records.find_one({'user_id': user.id})
    row = await flare.Row(registered(user.id), citations(user.id))
    if resp is None:
        response = (hikari.Embed(
            title=f"{user}'s profile",
            description="No profile found. What does this mean?\n\n> The user does not exist within the database. ",
            color="#2a2d31"
        )
        )
        await ctx.respond(response)
        return

    if resp['license'] is False:
        license = "Invalid"
    else:
        license = "Valid"

    response =( hikari.Embed(
        title=f"{user}'s profile",
        color="#2a2d31"
    )
    .set_thumbnail(user.avatar_url)
    .add_field(
        name="License",
        value=license,
        inline=True
    )
    .add_field(
        name="Registered Vehicles",
        value=f"{resp['vehicles'].count(resp['vehicles'])}",
        inline=True
    )
    .add_field(
        name="Citations",
        value=f"{resp['citations'].count(resp['citations'])}"
    )
    .set_footer(text="Centreville Roleplay", icon=bo.get_me().avatar_url)
    )
    msg = await ctx.respond(response, component=row)
def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")
