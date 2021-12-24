#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import re
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant

from bot import Bot
from config import AUTH_USERS, DOC_SEARCH, VID_SEARCH, MUSIC_SEARCH
from database.mdb import (
    savefiles,
    deletefiles,
    deletegroupcol,
    channelgroup,
    ifexists,
    deletealldetails,
    findgroupid,
    channeldetails,
    countfilters
)



@Client.on_message(filters.group & filters.command(["add"]))
async def addchannel(client: Bot, message: Message):

    if message.from_user.id not in AUTH_USERS:
        return

    try:
        cmd, text = message.text.split(" ", 1)
    except:
        await message.reply_text(
            "<i>ထည့်ပုံထည့်နည်းကမဟုပ်သေးဘူး သေချာကြည့်လုပ်ပါ!\n\n<code>/ဂရုစိုက်ပြန်လုပ်ပါ</code>  or\n"
            "<code>/add @channelusername</code></i>"
            "\n\nGet Channel id from @nas0055",
        )
        return
    try:
        if not text.startswith("@"):
            chid = int(text)
            if not len(text) == 14:
                await message.reply_text(
                    "နာမည်မှားနေတယ်နော် သေချာလုပ်ပါ"
                )
                return
        elif text.startswith("@"):
            chid = text
            if not len(chid) > 2:
                await message.reply_text(
                    "နာမည်မှားနေတယ်နော် သေချာလုပ်ပါ"
                )
                return
    except Exception:
        await message.reply_text(
            "နာမည်မှားနေတယ်နော် သေချာလုပ်ပါ\n"
            "ချက်အမှတ်က <b>-100xxxxxxxxxx</b> format\n"
            "ဂရုစိုက်ပြန်လုပ်ပါ",
        )
        return

    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<i>ဒီဘော့ကိုအက်မင်အနေနဲ့ထည့်ထားလေ - '၊ အက်မင်ထည့်ပီးပြန်လုပ်ပါ၊</i>",
        )
        return

    try:
        user = await client.USER.get_me()
    except:
        user.first_name =  " "

    try:
        await client.USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<i>User {user.first_name} အဲ့ချယ်နယ်မှာ ပိုင်ရှင်ကိုဘန်းရှင်သုံးလိုမရပါ။😡😡"
            "\n\nဂရုစိုက်ပြန်လုပ်ပါ🙄🙄 ပါမစ် ပေးပါ</i>",
        )
        return

    try:
        chatdetails = await client.USER.get_chat(chid)
    except:
        await message.reply_text(
            "<i>Send a message to your channel and try again</i>"
        )
        return

    intmsg = await message.reply_text(
        "<i>☺️ချယ်နယိကဒေတာတွေကိုကူးထည့်နေတာမို၊ခနစောင့်ပါ၊😍"
        "\n\n🙂ဒါက ဒေတာများရင်များသလောက်ကြာမှာပါ၊ ၁၀မိနစ်လောက်ပေါ့၊🙂"
        "\nတခြားဘာမှအမိန့်မပေးရဘူးနော်၊ကူးတာပျက်သွားမယ်🤨🤨!</i>"
    )

    channel_id = chatdetails.id
    channel_name = chatdetails.title
    group_id = message.chat.id
    group_name = message.chat.title

    already_added = await ifexists(channel_id, group_id)
    if already_added:
        await intmsg.edit_text("😏😏 Channel ka add p thar lay")
        return

    docs = []

    if DOC_SEARCH == "yes":
        try:
            async for msg in client.USER.search_messages(channel_id,filter='document'):
                try:
                    file_name = msg.document.file_name
                    file_id = msg.document.file_id
                    file_size = msg.document.file_size                   
                    link = msg.link
                    data = {
                        '_id': file_id,
                        'channel_id' : channel_id,
                        'file_name': file_name,
                        'file_size': file_size,
                        'link': link
                    }
                    docs.append(data)
                except:
                    pass
        except:
            pass

        await asyncio.sleep(5)

    if VID_SEARCH == "yes":
        try:
            async for msg in client.USER.search_messages(channel_id,filter='video'):
                try:
                    file_name = msg.video.file_name
                    file_id = msg.video.file_id   
                    file_size = msg.video.file_size              
                    link = msg.link
                    data = {
                        '_id': file_id,
                        'channel_id' : channel_id,
                        'file_name': file_name,
                        'file_size': file_size,
                        'link': link
                    }
                    docs.append(data)
                except:
                    pass
        except:
            pass

        await asyncio.sleep(5)

    if MUSIC_SEARCH == "yes":
        try:
            async for msg in client.USER.search_messages(channel_id,filter='audio'):
                try:
                    file_name = msg.audio.file_name
                    file_id = msg.audio.file_id   
                    file_size = msg.audio.file_size                 
                    link = msg.link
                    data = {
                        '_id': file_id,
                        'channel_id' : channel_id,
                        'file_name': file_name,
                        'file_size': file_size,
                        'link': link
                    }
                    docs.append(data)
                except:
                    pass
        except:
            pass

    if docs:
        await savefiles(docs, group_id)
    else:
        await intmsg.edit_text("Channel couldn't be added. Try after some time!")
        return

    await channelgroup(channel_id, channel_name, group_id, group_name)

    await intmsg.edit_text("ချယ်နယ်အက်တာပီးသွားပါပီ 🥳🥳")


@Client.on_message(filters.group & filters.command(["del"]))
async def deletechannelfilters(client: Bot, message: Message):

    if message.from_user.id not in AUTH_USERS:
        return

    try:
        cmd, text = message.text.split(" ", 1)
    except:
        await message.reply_text(
            "<i>ထည့်ပုံထည့်နည်းကမဟုပ်သေးဘူး သေချာကြည့်လုပ်ပါ!\n\n<code>/del channelid</code>  or\n"
            "<code>/del @channelusername</code></i>"
            "\n\nrun /filterstats to see connected channels",
        )
        return
    try:
        if not text.startswith("@"):
            chid = int(text)
            if not len(text) == 14:
                await message.reply_text(
                    "Enter valid channel ID\n\nrun /filterstats to see connected channels"
                )
                return
        elif text.startswith("@"):
            chid = text
            if not len(chid) > 2:
                await message.reply_text(
                    "နာမည်မှားနေတယ်နော် သေချာလုပ်ပါ"
                )
                return
    except Exception:
        await message.reply_text(
            "Enter a valid ID\n"
            "run /www.gg \n"
            "ဂရုစိုက်ပြန်လုပ်ပါ🙄🙄",
        )
        return

    try:
        chatdetails = await client.USER.get_chat(chid)
    except:
        await message.reply_text(
            "<i>User must be present in given channel.\n\n"
            "If user is already present, send a message to your channel and try again</i>"
        )
        returnDon't give any other commands now

    intmsg = await message.reply_text(
        "<i>အကုန်ဖျက်မှာနော်"
        "\n\nတခြားအမိန့်မပေးနဲ့ဦးဒါမပီးမချင်း!</i>"
    )

    channel_id = chatdetails.id
    channel_name = chatdetails.title
    group_id = message.chat.id
    group_name = message.chat.title

    already_added = await ifexists(channel_id, group_id)
    if not already_added:
        await intmsg.edit_text("ဘယ်လိုသုံးရင်ကောင်းမလဲ🙄🙄!")
        return

    delete_files = await deletefiles(channel_id, channel_name, group_id, group_name)
    
    if delete_files:
        await intmsg.edit_text(
            "ဖြုတ်ထားတယ် 😂!"
        )
    else:
        await intmsg.edit_text(
            "ဖြုတ်ထားတယ် 😂"
        )


@Client.on_message(filters.group & filters.command(["delall"]))
async def delallconfirm(client: Bot, message: Message):
    await message.reply_text(
        "ဖြုတ်ထားတယ် 😂",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="YES",callback_data="delallconfirm")],
            [InlineKeyboardButton(text="Yes",callback_data="delallcancel")]
        ])
    )


async def deleteallfilters(client: Bot, message: Message):

    if message.reply_to_message.from_user.id not in AUTH_USERS:
        return

    intmsg = await message.reply_to_message.reply_text(
        "<i>ဖြုတ်ထားတယ် 😂</i>"
        "\n\nဖြုတ်ထားတယ် 😂!</i>"
    )

    group_id = message.reply_to_message.chat.id

    await deletealldetails(group_id)

    delete_all = await deletegroupcol(group_id)

    if delete_all == 0:
        await intmsg.edit_text(
            "ဖြုတ်ထားတယ် 😂!"
        )
    elif delete_all == 1:
        await intmsg.edit_text(
            "Nothing to delete!!"
        )
    elif delete_all == 2:
        await intmsg.edit_text(
            "Couldn't delete filters. Try again after sometime.."
        )  


@Client.on_message(filters.group & filters.command(["filterstats"]))
async def stats(client: Bot, message: Message):

    if message.from_user.id not in AUTH_USERS:
        return

    group_id = message.chat.id
    group_name = message.chat.title

    stats = f"Stats for Auto Filter Bot in {group_name}\n\n<b>Connected channels ;</b>"

    chdetails = await channeldetails(group_id)
    if chdetails:
        n = 0
        for eachdetail in chdetails:
            details = f"\n{n+1} : {eachdetail}"
            stats += details
            n = n + 1
    else:
        stats += "\nNo channels connected in current group!!"
        await message.reply_text(stats)
        return

    total = await countfilters(group_id)
    if total:
        stats += f"\n\n<b>Total number of filters</b> : {total}"

    await message.reply_text(stats)


@Client.on_message(filters.channel & (filters.document | filters.video | filters.audio))
async def addnewfiles(client: Bot, message: Message):

    media = message.document or message.video or message.audio

    channel_id = message.chat.id
    file_name = media.file_name
    file_size = media.file_size
    file_id = media.file_id
    link = message.link

    docs = []
    data = {
        '_id': file_id,
        'channel_id' : channel_id,
        'file_name': file_name,
        'file_size': file_size,
        'link': link
    }
    docs.append(data)

    groupids = await findgroupid(channel_id)
    if groupids:
        for group_id in groupids:
            await savefiles(docs, group_id)
            
