import lightbulb
import hikari
import flare
from pymongo import MongoClient
import random
from bson.binary import UuidRepresentation

plugin = lightbulb.Plugin('', '')

bo = None
client = MongoClient("mongodb+srv://brncray:Bobrien@bot.lvf7vud.mongodb.net/?retryWrites=true&w=majority", uuidRepresentation='standard')


@plugin.command
@lightbulb.option('color', 'what color', type=str, required=True)
@lightbulb.option('license', 'what license plate', type=str, required=True)
@lightbulb.option('model', 'what model car', type=str, required=True)
@lightbulb.command('register', 'register a vehicle')
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd(ctx):
    db = client.get_database('data')
    license = None
    records = db.ticketing
    user = ctx.author
    resp = records.find_one({'user_id': user.id})
    if resp is None:
      records.insert_one({
          'user_id': user.id,
          'citations': [],
          'vehicles': [
            {
              "Model": ctx.options.model,
              "License": ctx.options.license,
              "Color": ctx.options.color,
              "id": random.randint(0,999999999999)
            }
          ],
          'license': False
      })
      response = (        
        hikari.Embed(
          title="Car Registered", 
          color="#2a2d31"
      ).add_field('Model:', value=ctx.options.model, inline=True)
      .add_field('License:', value=ctx.options.license, inline=True)
      .add_field('Color:', value=ctx.options.color, inline=True)
      )
      await ctx.respond(response)
      return
    upd = {
      "Model": ctx.options.model,
      "License": ctx.options.license,
      "Color": ctx.options.color,
      "id": random.randint(0,999999999999)
      }
    records.update_one({'user_id': user.id}, {'$push': {'vehicles':upd}})
    response = (        
      hikari.Embed(
        title="Car Registered", 
        color="#2a2d31"
    ).add_field('Model:', value=ctx.options.model, inline=True)
    .add_field('License:', value=ctx.options.license, inline=True)
    .add_field('Color:', value=ctx.options.color, inline=True)
    )
    await ctx.respond(response, flags=hikari.MessageFlag.EPHEMERAL)


def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")
