# Auto Filter Bot V1.5





#### ဒါကို ဒီလိုခေါ်ပါတယ်😁😁 :D
#### This is Version 1.5 of [AFB](https://github.com/konay1122/Auto-Filter-Bot)
#### Bot simply search for the files from provided channel according to given query and gives link to those files as buttons!

## ဘယ်လိုသုံးရင်ကောင်းမလဲ🙄🙄
* Add bot to your group with admin rights.

* Add bot to all channels which you want to link with all admin rights!

## Bot Commands - Works in Group only

(You need to be a Auth User in order to use these commands)

* /add channelid  -  
or
* /add @channelusername - 

<i>NOTE : You can get your channel ID from @nas0055 </i>


* /del channelid  -  
or
* /del @channelusername  -  

<i>NOTE : You can get connected channel details by /filterstats </i>


* /delall  -  

* /filterstats  -  .

## You can check the video tutorial on how to deploy

[Click here to see tutorial video](https://www.youtube.com/watch?v=XHr7vaHJvq4)

Thanks to [GG](https://telegram.dog/nas0055) and [NAS](https://telegram.dog/nas0055) for the video

## Any bugs or errors or suggestions, report at [NAS](https://t.me/nas0055)


## Installation

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TroJanzHEX/Auto-Filter-Bot-V2)

### Deploy in your vps
```sh
git clone https://github.com/TroJanzHEX/Auto-Filter-Bot-V2
cd Auto-Filter-Bot-V2
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
```

## Configs

* TG_BOT_TOKEN  - Get bot token from @BotFather

* APP_ID        - From my.telegram.org (or @UseTGXBot)

* API_HASH      - From my.telegram.org (or @UseTGXBot)

* TG_USER_SESSION  - A pyrogram user session string. Generate by [clicking here](https://repl.it/@prgofficial/String-Gen)

* AUTH_USERS  - ID of users that can use the bot commands. Get from [MissRose Bot](https://telegram.dog/MissRose_bot) by using /id command

* DATABASE_URI  - Mongo Database URL from https://cloud.mongodb.com/

* DATABASE_NAME  - Your database name from mongoDB. Default will be 'Cluster0'

* DOC_SEARCH  - Should bot search for document files ( Give 'yes' or 'no' )

* VID_SEARCH  - Should bot search for video files ( Give 'yes' or 'no' )

* MUSIC_SEARCH  - Should bot search for music files ( Give 'yes' or 'no' )

## Credits

[![TroJanz](https://img.shields.io/badge/Pyrogram%20-%23F37626.svg?&style=for-the-badge&logo=telegram&logoColor=white)](https://github.com/pyrogram/pyrogram)

And as always, [SpEcHlDe](https://telegram.dog/SpEcHlDe)
