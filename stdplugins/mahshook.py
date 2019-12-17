"""Emoji

Available Commands:

.m"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    if input_str == "m":
        await event.edit(input_str)
        animation_chars = [
            "ⓂⒶⒽⓈⒽⓄⓄⓀ",
            "🅜🅐🅗🅢🅗🅞🅞🅚",
            "M҉A҉H҉S҉H҉O҉O҉K҉",
            "mαhshσσk",
            "爪卂卄丂卄ㄖㄖҜ",
            "₥₳Ⱨ₴ⱧØØ₭",
            "ᎷᏗᏂᏕᏂᎧᎧᏦ",
            "๓คђรђ๏๏к",
            "ɱåȟ§ȟ¤¤ķ",
            "ϻÃĤŜĤỖỖЌ",
            "ომhჰhõõκ",
            "ꁒꋫꑛꌚꑛꆂꆂꀗ",
            "MƛӇƧӇƠƠƘ",
            "mαhšh⊕⊕κ",
            "ṀḀḦṠḦṎṎḲ",
            "🄼🄰🄷🅂🄷🄾🄾🄺",
            "M͎A͎H͎S͎H͎O͎O͎K͎",
            "M̺A̺H̺S̺H̺O̺O̺K̺",
            "M̳A̳H̳S̳H̳O̳O̳K̳",
            "M̷A̷H̷S̷H̷O̷O̷K̷",
            "M̴A̴H̴S̴H̴O̴O̴K̴",
            "M̶A̶H̶S̶H̶O̶O̶K̶",
            "M̷̨̦͙̗̭̞͓̘̖̓͌̉͐̄̃̾͗Ầ̶̧̢̳̰͉̖͉̩̰͚͗H̴͖̰͛̑̄́̏̚Ṣ̴̰̽̾̂̂H̷̡͔͖̘̱̱͓̀̄̐͌̚Ȯ̸̩̜̜̮̯̬́͑̈́͒̃͊̆̉̚O̶̜̹̼̞̤̒͒̽̔͆͒K̸̡͓͎͉̳̰̯̅̈̈́́̎̓",
            "๓คђรђ๏๏к",
            "ʍǟɦֆɦօօӄ",
            "๓คhŞh໐໐k",
            "ＭΛＨＳＨ♢♢Ｋ",
            "ʍǟɦֆɦօօӄ",
            "ᎷᏗᏂᏕᏂᎧᎧᏦ",
            "MÄH§HÖÖK",
            "M̷A̷H̷S̷H̷O̷O̷K̷",
            "ᘻᗩᕼSᕼᓍᓍᖽᐸ",
            "🤖**__MAHSHOOK__**🤖"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 20])
