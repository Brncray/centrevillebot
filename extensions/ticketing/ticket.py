import lightbulb
import hikari
import flare
from pymongo import MongoClient
plugin = lightbulb.Plugin('', '')

bo = None
client = MongoClient("mongodb+srv://brncray:Bobrien@bot.lvf7vud.mongodb.net/?retryWrites=true&w=majority")

penal_codes_cod = ['(1)01', '(1)02', '(1)03', '(1)04', '(1)05', '(1)06', '(1)07', '(1)08', '']
penal_codes_ref = ['(1)01 Intimidation (Major)', '(1)02 Intimidation (Minor)', '(1)03 Assault', '(1)04 Assault on LEO / Gov. Worker', '(1)05 Aggravated Assault', '(1)06 Battery', '(1)07 Aggravated Battery', '(1)08 Attempted Murder']
penal_codes_cha = ['$1000 + 30 sec jail time', '$500', '$1000 + 60 sec jail time', '$1500 + 90 sec jail time', '$1500 + 90 sec jail time', '$500 + 30 jail time', '$1000 + 60 sec jail time', '$2000 + 120 sec jail time | 2nd Degree (200 Seconds; $2500)']
@plugin.command
@lightbulb.option('charge4', 'what charge', choices=penal_codes_ref, required=False)
@lightbulb.option('charge3', 'what charge', choices=penal_codes_ref, required=False)
@lightbulb.option('charge2', 'what charge', choices=penal_codes_ref, required=False)
@lightbulb.option('dep', 'what department', choices=['Outagamie County Sheriff\'s Office', 'Wisconsin State Patrol'], required=True)
@lightbulb.option('charge1', 'what charge', choices=penal_codes_ref, required=True)
@lightbulb.option('user', 'what user', type=hikari.Member, required=True)
@lightbulb.command('ticket', 'ticket a user')
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd(ctx):
    db = client.get_database('data')
    license = None
    records = db.ticketing
    user = ctx.options.user

    def get_first_word(input_string):
        words = input_string.split()
        if words:
            return words[0]
        else:
            return None

    charge1 = ctx.options.charge1
    charge2 = ctx.options.charge2
    charge3 = ctx.options.charge3
    charge4 = ctx.options.charge4
    charge1_ind = penal_codes_cod[penal_codes_cod.index(get_first_word(charge1))]
    charge1_pro = penal_codes_cha[penal_codes_cod.index(get_first_word(charge1))]
    try:
        charge2_pro = penal_codes_cha[penal_codes_cod.index(get_first_word(charge2))]
        charge2_ind = penal_codes_cod[penal_codes_cod.index(get_first_word(charge2))]
    except Exception:
        charge2_pro = ""
        charge2_ind = ""
        pass
    try:
        charge3_pro = penal_codes_cha[penal_codes_cod.index(get_first_word(charge3))]
        charge3_ind = penal_codes_cod[penal_codes_cod.index(get_first_word(charge3))]
    except Exception:
        charge3_pro = ""
        charge3_ind = ""
        pass

    try:
        charge4_pro = penal_codes_cha[penal_codes_cod.index(get_first_word(charge4))]
        charge4_ind = penal_codes_cod[penal_codes_cod.index(get_first_word(charge4))]
    except Exception:
        charge4_pro = ""
        charge4_ind = ""
        pass

    charges = charge1_ind + " " + charge2_ind + " " + charge3_ind + " " + charge4_ind + " "
    due = charge1_pro + " + " + charge2_pro + " + " + charge3_pro + " + " + charge4_pro
    resp = records.find_one({'user_id': user.id})
    if ctx.options.dep == "Outagamie County Sheriff\'s Office":
        prefix = "Deputy "
    if ctx.options.dep == "Wisconsin State Patrol":
        prefix = "Trooper "
    if ctx.options.dep == "FVMPD":
        prefix = "Officer "
    if resp is None:
        records.insert_one({
            'user_id': user.id,
            'citations': [{
                'Charges': charges,
                'Ticketed by': f"{prefix}<@{ctx.author.id}>",
                'Department': ctx.options.dep,
                'Amount due': f"Due: {due}"
            }],
            'vehicles': [],
            'license': False
        })
        dm_channel = bo.cache.get_dm_channel_id(user.id) # from cache
        dm_channel = await bo.rest.create_dm_channel(user.id) # from rest api; more reliable. store this for later uses
        ...
  
        # when you want to send the message
        emb = hikari.Embed(
          title="Citation Recieved",
          description=f"Penal Codes: **{charges}**\nDepartment: {ctx.options.dep}\nOfficer: {prefix}<@{ctx.author.id}>\nDue: {due}",
          color="#2a2d31"
        )
        await dm_channel.send(embed=emb)
        emb = hikari.Embed(
          title="Citation Sent",
          description=f"Penal Codes: **{charges}**\nDepartment: {ctx.options.dep}\nOfficer: {prefix}<@{ctx.author.id}>\nDue: {due}",
          color="#2a2d31"
        )
        await ctx.respond(embed=emb, flags=hikari.MessageFlag.EPHEMERAL)
        return
    upd = {
      'Charges': charges,
      'Ticketed by': f"{prefix}<@{ctx.author.id}>",
      'Department': ctx.options.dep,
      'Amount due': f"Due: {due}"
}
    records.update_one({'user_id': user.id}, {'$push': {'citations':upd}})
    dm_channel = bo.cache.get_dm_channel_id(user.id) # from cache
    dm_channel = await bo.rest.create_dm_channel(user.id) # from rest api; more reliable. store this for later uses
    ...
  
    # when you want to send the message
    emb = hikari.Embed(
      title="Citation Recieved",
      description=f"Penal Codes: **{charges}**\nDepartment: {ctx.options.dep}\nOfficer: {prefix}<@{ctx.author.id}>\nDue: {due}",
      color="#2a2d31"
    )
    await dm_channel.send(embed=emb)
    emb = hikari.Embed(
      title="Citation Sent",
      description=f"Penal Codes: **{charges}**\nDepartment: {ctx.options.dep}\nOfficer: {prefix}<@{ctx.author.id}>\nDue: {due}",
      color="#2a2d31"
    )
    await ctx.respond(embed=emb, flags=hikari.MessageFlag.EPHEMERAL)


def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")
