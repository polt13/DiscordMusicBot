from discord.ext import commands
from discord import FFmpegOpusAudio
import discord
from yt_dlp import YoutubeDL

prefix = "$"

ydl_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "nocheckcertificate": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",  # bind to ipv4 since ipv6 addresses cause issues sometimes
    "cachedir": False,
}
ffmpeg_options = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}

embeds = {
    "help": discord.Embed(
        title="How to use",
        type="rich",
        description="\n\n Prefix every **command** with '$' \n\n š£ **p** / **play** queues/plays a track (title or url) or a playlist (url only)\n\n š£ **skip** / **next** skips to next track in queue\n\n š£ **list** / **dq** displays current queue \n\n š£ **pau** pauses, **res** resumes and **dc** disconnects the bot from the VC \n\n š£ **now** shows currently playing song\n\nš£ **clear** clears the queue\n\n š£ **stop** clears queue and stops current session \n\n š£ **remove** / **rq** *track* to remove a track from a queue\n\n š£ **swap** *track1* *track2* to switch the order of two tracks in the queue\n\n",
    ),
    "not_connected": discord.Embed(
        title="Not connected to a voice channel š¦”", color=discord.Color.teal()
    ),
    "connected_already": discord.Embed(
        title="Already connected to a different voice channel š³",
        color=discord.Color.teal(),
    ),
    "empty_queue": discord.Embed(title="Queue is empty š“", color=discord.Color.teal()),
    "no_audio": discord.Embed(
        title="Not playing any audio š§āāļø", color=discord.Color.teal()
    ),
    "pause": discord.Embed(title="āø Paused track.", color=discord.Color.teal()),
    "resume": discord.Embed(title="āÆ Resumed track.", color=discord.Color.teal()),
    "stop": discord.Embed(
        title="ā¹ Music stopped and queue cleared", color=discord.Color.teal()
    ),
}
