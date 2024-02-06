import lightbulb
import hikari
import flare
from pymongo import MongoClient
import pymongo

plugin = lightbulb.Plugin('', '')

bo = None
client = MongoClient("mongodb+srv://brncray:Bobrien@bot.lvf7vud.mongodb.net/?retryWrites=true&w=majority")

@plugin.command
@lightbulb.add_checks(
    lightbulb.has_roles(1203078168282406912)
)
@lightbulb.command('claim_license', 'claim your license', auto_defer=False)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cmd(ctx):
    db = client.get_database('data')
    license = None
    records = db.ticketing
    user = ctx.author

    resp = records.find_one({'user_id': user.id})

    if resp is None:
      records.insert_one({
          'user_id': user.id,
          'citations': [[]],
          'vehicles': [{}],
          'license': True
      })
      await ctx.respond('You\'re license has been claimed! Use /profile to verify', flags=hikari.MessageFlag.EPHEMERAL)

    else:
      if resp['license'] == True:
        await ctx.respond('You already have a license!', flags=hikari.MessageFlag.EPHEMERAL)
      else:
        records.update_one({'user_id': user.id}, {'$set': {'license': True}})
        await ctx.respond('You\'re license has been claimed! Use /profile to verify', flags=hikari.MessageFlag.EPHEMERAL)


def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")
