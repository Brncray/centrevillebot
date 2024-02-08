import lightbulb
import hikari
import flare
from pymongo import MongoClient
import pymongo

plugin = lightbulb.Plugin('', '')

bo = None
client = MongoClient("mongodb+srv://brncray:Bobrien@bot.lvf7vud.mongodb.net/?retryWrites=true&w=majority")

@plugin.command
@lightbulb.option('id', 'The ID number is listed below the registed vehicle', type=int, required=True)
@lightbulb.command('unregister', 'unregister a vehicle', auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd(ctx):
    db = client.get_database('data')
    license = None
    records = db.ticketing
    user = ctx.author

    resp = records.find_one({'user_id': user.id})

    if resp is None:

        response = (hikari.Embed(
            title=f"Error",
            description="You are not registed within the database! This means you do not have any vehicles to register. To create a profile:\n> Register a car",
            color="#2a2d31"
        )
        )
        await ctx.respond(response)
        return
      # Print or use the result documents
    query = {"vehicles.id": ctx.options.id}  # Replace with your specific query
    update = {"$pull": {"vehicles": {"id": ctx.options.id}}}
    result = records.update_one(query, update)
  
    
    response = hikari.Embed(
      title="Vehicle Removed",
      description=f"Removed registration for the vehicle with the ID: {ctx.options.id}",
      color="#2a2d31"
    )
    await ctx.respond(response, flags=hikari.MessageFlag.EPHEMERAL)



def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")
