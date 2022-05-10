@bot.command()
async def unlock(ctx, channel: nextcord.TextChannel=None, type=None):
    if channel == None:
        channel = ctx.message.channel
    if type == "--server":
        for channel in guild.channels:
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("Server was unlocked")
    else:
        await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(f"{channel} was unlocked.")
