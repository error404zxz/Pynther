import hikari
import lightbulb


file = open(r"C:\projectz\botdata.txt", "r")
bot_start_raw_data = file.read()
print(bot_start_raw_data)
bot_start_data = bot_start_raw_data.split('\n')
print(bot_start_data)
bot_token = bot_start_data[1]
guild = int(bot_start_data[0])
bot = lightbulb.BotApp(token=bot_token,
                       default_enabled_guilds=(guild))


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Pynther is alive")


@bot.command
@lightbulb.command('hello', 'hello there')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond('hello there')

@bot.command
@lightbulb.command('group', 'the group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def group(ctx):
    pass
@group.child
@lightbulb.command('subcommand', 'the subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    ctx.respond('yeah, this is a sub command')

@bot.command
@lightbulb.option('numm1', 'the first number', type=int)
@lightbulb.option('numm2', 'the second number', type=int)
@lightbulb.command('addd', 'add 2 options together')
@lightbulb.implements(lightbulb.SlashCommand)
async def addd(ctx):
    await ctx.respond(ctx.options.numm1 + ctx.options.numm2)


bot.run()
