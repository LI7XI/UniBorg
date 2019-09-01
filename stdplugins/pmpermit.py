"""Personal Message Spammer
Available Commands:
.approve
.block
.list approved pms"""
import asyncio
import json
from telethon import events
from telethon.tl import functions, types
from sql_helpers.pmpermit_sql import is_approved, approve, disapprove, get_all_approved
from uniborg.util import admin_cmd


global PM_WARNS
global PREV_REPLY_MESSAGE
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}


BAALAJI_TG_USER_BOT = "Hi! I will answer to your message soon. Please wait for my response and don't spam my PM. Thanks"
TG_COMPANION_USER_BOT = "Please wait for his response and don't spam his PM."
UNIBORG_USER_BOT_WARN_ZERO = "I FUCKING TOLD U TO FUCKING NOT DO FUCKING ANYTHING.😡\n!!!BLOCKAGE ACTIVATED!!!"
UNIBORG_USER_BOT_NO_WARN = "Hi! My Master has not yet taken note of you in his OFFICE!\nLet me call him and wait right over here and don't do anything😊.\nDoing anything will result in blockage of chat.👿"


@borg.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(event):
    global PM_WARNS
    global PREV_REPLY_MESSAGE
    sender = await event.get_sender()
    current_message_text = event.message.message.lower()
    BAALAJI_TG_USER_BOT = "Hi! I will answer to your message soon. Please wait for my response and don't spam my PM. Thanks"
    TG_COMPANION_USER_BOT = "Please wait for his response and don't spam his PM."
    UNIBORG_USER_BOT_WARN_ZERO = "I FUCKING TOLD U TO FUCKING NOT DO FUCKING ANYTHING.😡\n!!!BLOCKAGE ACTIVATED!!!"
    UNIBORG_USER_BOT_NO_WARN = "Hi! My Master has not yet taken note of you in his OFFICE!\nLet me call him and wait right over here and don't do anything😊.\nDoing anything will result in blockage of chat.👿"
    if current_message_text == BAALAJI_TG_USER_BOT or current_message_text == TG_COMPANION_USER_BOT or current_message_text == UNIBORG_USER_BOT_NO_WARN or current_message_text == UNIBORG_USER_BOT_WARN_ZERO:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if Config.NO_P_M_SPAM and not sender.bot:
        chat = await event.get_chat()
        if not is_approved(chat.id) and chat.id != borg.uid:
            logger.info(chat.stringify())
            logger.info(PM_WARNS)
            if chat.id not in PM_WARNS:
                PM_WARNS.update({chat.id: 0})
            if PM_WARNS[chat.id] == Config.MAX_FLOOD_IN_P_M_s:
                r = await event.reply(UNIBORG_USER_BOT_WARN_ZERO)
                await asyncio.sleep(3)
                await borg(functions.contacts.BlockRequest(chat.id))
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                PREV_REPLY_MESSAGE[chat.id] = r
                return
            r = await event.reply(UNIBORG_USER_BOT_NO_WARN)
            PM_WARNS[chat.id] += 1
            if chat.id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat.id].delete()
            PREV_REPLY_MESSAGE[chat.id] = r


@borg.on(admin_cmd("approvepm ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    global PM_WARNS
    global PREV_REPLY_MESSAGE
    reason = event.pattern_match.group(1)
    chat = await event.get_chat()
    if Config.NO_P_M_SPAM:
        if event.is_private:
            if not is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                approve(chat.id, reason)
                await event.edit("Private Message Accepted")
                await asyncio.sleep(3)
                await event.delete()


@borg.on(admin_cmd("blockpm ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    global PM_WARNS
    global PREV_REPLY_MESSAGE
    reason = event.pattern_match.group(1)
    chat = await event.get_chat()
    if Config.NO_P_M_SPAM:
        if event.is_private:
            if is_approved(chat.id):
                disapprove(chat.id)
                await event.edit(".................../´¯/) \n.................,/¯../ \n................/..../ \n........../´¯/'...'/´¯¯`·¸ \n....../'/.../..../......./¨¯\ \n.....('(...´...´.... ¯~/'...') \n......\.................'...../ \n.......''...\.......... _.·´ \n.........\..............( \n...........\.............\...\n\nFuck Off Bitch")
                await asyncio.sleep(3)
                await borg(functions.contacts.BlockRequest(chat.id))


@borg.on(admin_cmd("list approved pms"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    global PM_WARNS
    global PREV_REPLY_MESSAGE
    approved_users = get_all_approved()
    APPROVED_PMs = "Current Approved PMs\n"
    for a_user in approved_users:
        if a_user.reason:
            APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
        else:
            APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
    if len(APPROVED_PMs) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
            out_file.name = "approved.pms.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Current Approved PMs",
                reply_to=event
            )
            await event.delete()
    else:
        await event.edit(APPROVED_PMs)
