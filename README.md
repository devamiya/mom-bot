![Solid](https://img.icons8.com/color/96/000000/bot.png)
# Momaizer
#### MoM Summarizer

<!-- [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) -->

Momaizer is a is an automatic meeting transcription system with real-time recognition and summarization capabilities. 

## Prerequisite
- [Python](https://www.python.org/)
- [NodeJS](https://nodejs.org/en/), fully tested on NodeJS 14, 16
- A Microsoft 365 account. If you do not have Microsoft 365 account, apply one from [Microsoft 365 developer program](https://developer.microsoft.com/en-us/microsoft-365/dev-program)
- Latest [Teams Toolkit Visual Studio Code Extension](https://aka.ms/teams-toolkit) or [TeamsFx CLI](https://aka.ms/teamsfx-cli)
- An [Azure subscription](https://azure.microsoft.com/en-us/free/)


## Run the Momaizer Teams App
1. Clone the repo to your local workspace or directly download the source code.
1. Download [Visual Studio Code](https://code.visualstudio.com) and install [Teams Toolkit Visual Studio Code Extension](https://aka.ms/teams-toolkit).
1. Open the project in Visual Studio Code.
1. Once deployment is completed, you can preview the app running in Azure. In Visual Studio Code, open `Run and Debug` and select `Launch Remote (Edge)` or `Launch Remote (Chrome)` in the dropdown list and Press `F5` or green arrow button to open a browser.
1. Add to the teams local

![1](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/1.jpg)


## Run the Momaizer Teams App
1. Once any meeting over open it in teams
2. Copy the meeting url and download the meeting transcript(optional)
3. Send the link to the Momaizer

![2](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/2.jpg)

![3](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/3.jpg)
![4](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/4.jpg)

Copy the message into the Transformater(Transcript formatter) folder as below
![5](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/5.jpg)

Then move to the  ``TransFormater folder`` and run the below command
 ```sh
    npm install
    node index.js
```
It will generate the formatted text for the summarization 
![6](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/6.jpg)

Original Transcript file looks like as below
![31](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/31.jpg)

Then run the ``summarizer.py`` to generate the summary of the transcript [link to colab](https://colab.research.google.com/drive/17yRBgS82DWtEEz_aE22Iw51UHQuael8A#scrollTo=kBvGuslhUEYJ)
![7](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/7.jpg)

Once the summary generated the bot will pick the details and notify in the Momaizer

Just run the post request ``http://localhost:3978/api/notification``
![8](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/8.jpg)


Finally the meeting summary will be shown as below
![9](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/9.jpg)

Also the Email, Issue and Task can be created directly with one click
![10](https://github.com/devamiya/mom-bot/blob/main/Momaizer/images/10.jpg)

## Team - Code Raiders
1. Amiya Panigrahi
1. Priyanka Tomar
1. Anita Naikwadi
1. Saksham Taletia
1. Vishal Patil

## #CoPBrainTrickler #2022




## License

MIT

**Free Software, Hell Yeah!**