import lightbulb
import hikari
import flare
from pymongo import MongoClient
import pymongo

plugin = lightbulb.Plugin('', '')

bo = None
client = MongoClient(
    "mongodb+srv://brncray:Bobrien@bot.lvf7vud.mongodb.net/?retryWrites=true&w=majority"
)


@flare.button(label="Reset", style=hikari.ButtonStyle.DANGER)
async def reset(ctx: flare.MessageContext, ) -> None:
  db = client.get_database('data')
  records = db.ticketing
  update = {"$set": {"citations": [{}]}}
  records.update_many({}, update)
  update = {"$set": {"vehicles": [{}]}}
  records.update_many({}, update)
  await ctx.respond('Database has been reset',
                    flags=hikari.MessageFlag.EPHEMERAL)


@plugin.command
@lightbulb.command('reset', 'reset database', auto_defer=False)
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd(ctx):
  license = None
  row = await flare.Row(reset())

  emb = hikari.Embed(
      title="Confirm Deletion",
      description="Are you sure you want to reset the database? This will **permanently delete** all citations and registered vehicles",
      color="#FF0000")
  await ctx.respond(emb, component=row, flags=hikari.MessageFlag.EPHEMERAL)


def load(bot):
  global bo
  bo = bot
  bot.add_plugin(plugin)
  print("Successfully loaded")
