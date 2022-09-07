import hikari
import lightbulb
bot = lightbulb.BotApp(token='',
                       default_enabled_guilds=())


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
async def (ctx):
    ctx.respond('yeah, this is a sub command')

@bot.command
 @lightbulb.option('numm1', 'the first number', type=int)
 @lightbulb.option('numm2', 'the second number', type=int)
 @lightbulb.command('addd', 'add 2 options together')
  @lightbulb.implements(lightbulb.SlashCommand)
  async def addd(ctx):
     await ctx.respond(ctx.options.numm1 + ctx.options.numm2)


bot.run()
