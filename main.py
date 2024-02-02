import flare
import lightbulb
import hikari
import io
import os



bot = lightbulb.BotApp(
    token='',
    intents=hikari.Intents.ALL,
    prefix="-"
)
flare.install(bot)

# @bot.listen(hikari.GuildMessageCreateEvent)
# async def print_message(event):
#    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started.')



@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"Something went wrong during invocation of command `{event.context.command.name}`.")
        raise event.exception

    # Unwrap the exception to get the original cause
    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("You are not the owner of this bot.")
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.")
    elif isinstance(exception, lightbulb.MissingRequiredRole):
        await event.context.respond(f"You are missing a required role. If you think this is a mistake please contact an administrator.")



bot.load_extensions_from('extensions/session')







bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name="Watching sessions",
        url="https://discord.gg/centreville",
        type=hikari.ActivityType.STREAMING,
    ),
)

