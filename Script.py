class script(object):

    START_TXT = """<b>🎉 I’m #Doom</b>

<b>ʜᴇʏ {}, 👋</b>

<b>🍿 Unlimited Movies & Series</b>
<b>🆓 100% Free, Always</b>
<b>🎬 Movies • Series • Webshows</b>

<b>⚡ Powered By <a href="https://t.me/tokyohdseries">BERLIN 🎭</a></b>
"""

    GSTART_TXT = """<b>🎉 I’m #Doom</b>

<b>ʜᴇʏ {}, 👋</b>

<b>🍿 Unlimited Movies & Series</b>
<b>🆓 100% Free, Always</b>
<b>🎬 Movies • Series • Webshows</b>

<b>⚡ Powered By <a href="https://t.me/tokyohdseries">BERLIN 🎭</a></b>
"""

    HELP_TXT = """<b>
✨ How to Request Movies / Series ✨  

➤ Google the correct name  
➤ Send name in group  

📌 Movies  
➤ Movie Name + Year  
Ex: Damsel 2024  

📌 Series  
➤ Series Name + S01  
Ex: Loki S01  

⚡ Powered By BERLIN 🎭
</b>"""

    ABOUT_TXT = """<b>╭────[ ʙᴏᴛ ᴅᴇᴛᴀɪʟs ]────⍟
├⍟ Mʏ Nᴀᴍᴇ : Doom
├⍟ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href="https://t.me/UPROFESESR">OWNER 🎭</a>
├⍟ Lɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ
├⍟ Lᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 𝟹
├⍟ Dᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ
├⍟ Bᴏᴛ Sᴇʀᴠᴇʀ : ʀᴇɴᴅᴇʀ
├⍟ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ1.4 [ ꜱᴛᴀʙʟᴇ ]
╰───────────────⍟</b>"""

    CHANNELS = """<b>
⚡ TOKYOVERSE Network ⚡  

▫ Latest Movies & Series  
▫ Fast Search  
▫ 24×7 Online  

🔗 Updates : <a href="https://t.me/tokyohdseries">Join</a>
</b>"""

    CAPTION = """<b><a href="https://t.me/tokyohdseries">{file_name}</a></b>

<b>⚜️ Powered By : <a href="https://t.me/tokyohdseries">BERLIN 🎭</a></b>"""

    IMDB_TEMPLATE_TXT = """<b>
<a href={url}>{title} ({year})</a>

⭐ Rating : {rating}  
🎭 Genre : {genres}  
🎧 Audio : {languages}

<b>Requested By :</b> {message.from_user.mention}
</b>"""

    DISCLAIMER_TXT = """<b>
This bot does not host any files.
All content is indexed from Telegram.

If you are a copyright owner,
contact admin for removal.
</b>"""

    LOGO = r"""
████████╗ ██████╗ ██╗  ██╗██╗   ██╗ ██████╗ ██╗   ██╗███████╗██████╗ ███████╗
╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██╔══██╗██╔════╝
   ██║   ██║   ██║█████╔╝  ╚████╔╝ ██║   ██║██║   ██║█████╗  ██████╔╝███████╗
   ██║   ██║   ██║██╔═██╗   ╚██╔╝  ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║
   ██║   ╚██████╔╝██║  ██╗   ██║   ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║███████║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝

          🎬  TOKYOVERSE  🎬
      Movies • Series • Webshows
        Powered By BERLIN 🎭
"""
