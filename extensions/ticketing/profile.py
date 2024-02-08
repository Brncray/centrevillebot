import lightbulb
import hikari
import flare
from pymongo import MongoClient
import asyncio

plugin = lightbulb.Plugin('', '')

bo = None
client = MongoClient(
    "mongodb+srv://brncray:Bobrien@bot.lvf7vud.mongodb.net/?retryWrites=true&w=majority"
)
wsp = 1099918152990732296
ocso = 1099918152990732290

  
@flare.button(label="Registered Vehicles", style=hikari.ButtonStyle.PRIMARY)
async def registered(ctx: flare.MessageContext, user_id: int) -> None:
  has_roles = False
  if wsp in ctx.member.role_ids:
    has_roles = True
  if ocso in ctx.member.role_ids:
    has_roles = True

  if user_id != ctx.author.id and has_roles == False:
    emb = hikari.Embed(
        title="You cannot view this user's profile!",
        description=
        "You are not able to view another user's registered vehicles unless you are a LEO!",
        color="#2a2d31")
    await ctx.respond(embed=emb, flags=hikari.MessageFlag.EPHEMERAL)
    return
  db = client.get_database('data')
  records = db.ticketing
  resp = records.find_one({'user_id': user_id})
  arr = resp.get("vehicles", [])
  string = ""
  documents = records.find({'user_id': user_id})
  for document in documents:
    # Access the array field
    array_field = document.get(
        "vehicles"
    )  # Replace "array_field_name" with the name of your array field

    # Check if the array field exists and is not empty
    if array_field:
      # Iterate over each object in the array
      for obj in array_field:
        first_item = True
        # Iterate over each field in the object
        try:
          for key, value in obj.items():

            if first_item:
              value = f"**{value}**"
              first_item = False
            # Concatenate each field and value into the result string
            string += f"{key}: {value}\n"
          string += "-------------------------\n"
        except AttributeError:
          await ctx.respond(hikari.Embed(title="Citations",
                                         description="No vehicles found!",
                                         color="#2a2d31"),
                            flags=hikari.MessageFlag.EPHEMERAL)
          return
      response = (hikari.Embed(title=f"Registered Vehicles",
                               description=f"{string}",
                               color="#2a2d31").set_footer(
                                   text="Centreville Roleplay",
                                   icon=bo.get_me().avatar_url))
      await ctx.respond(response, flags=hikari.MessageFlag.EPHEMERAL)


@flare.button(label="Citations", style=hikari.ButtonStyle.PRIMARY)
async def citations(ctx: flare.MessageContext, user_id: int) -> None:

  db = client.get_database('data')
  records = db.ticketing
  resp = records.find_one({'user_id': user_id})
  arr = resp.get("citations", [])
  string = ""

  documents = records.find({'user_id': user_id})
  for document in documents:
    # Access the array field
    array_field = document.get(
        "citations"
    )  # Replace "array_field_name" with the name of your array field

    # Check if the array field exists and is not empty
    if array_field:
      # Iterate over each object in the array
      for obj in array_field:
        first_item = True
        # Iterate over each field in the object
        try:
          for key, value in obj.items():

            if first_item:
              value = f"**{value}**"
              first_item = False
            # Concatenate each field and value into the result string
            string += f"{key}: {value}\n"
          string += "-------------------------\n"
        except AttributeError:
          await ctx.respond(hikari.Embed(title="Citations",
                                         description="No citations found!",
                                         color="#2a2d31"),
                            flags=hikari.MessageFlag.EPHEMERAL)
          return

  response = (hikari.Embed(title=f"Citations",
                           description=f"{string}",
                           color="#2a2d31").set_footer(
                               text="Centreville Roleplay",
                               icon=bo.get_me().avatar_url))
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
    records.insert_one({
        'user_id': user.id,
        'citations': [{}],
        'vehicles': [{}],
        'license': False
    })
    resp = records.find_one({'user_id': user.id})

  if resp['license'] is False:
    license = "Invalid"
  else:
    license = "Valid"

  response = (hikari.Embed(
      title=f"{user}'s profile",
      color="#2a2d31").set_thumbnail(user.avatar_url).add_field(
          name="License", value=license,
          inline=True).set_footer(text="Centreville Roleplay",
                                  icon=bo.get_me().avatar_url))
  msg = await ctx.respond(response, component=row)


def load(bot):
  global bo
  bo = bot
  bot.add_plugin(plugin)
  print("Successfully loaded")
