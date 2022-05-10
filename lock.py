@bot.command()
async def lock(ctx, channel: nextcord.TextChannel=None, type=None):
    if channel == None:
        channel = ctx.message.channel
    if type == "--server":
        for channel in guild.channels:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("Server was locked")
    else:
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(f"{channel} was locked.")
