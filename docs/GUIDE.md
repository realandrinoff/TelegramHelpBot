<h1>Complete guide to help bot in Telegram</h1>


## 📝 Table of Contents

- [1️⃣ Downloading dependencies](#dependencies)
- [2️⃣ - Creating a bot](#creating)
- [3️⃣ - Configuring the bot](#config)
- [4️⃣ - Setting up virtual environment](#venv)
- [5️⃣ - Deploying](#deployment)
- [How to customize](#customization)

____
## 📩 Downloading the dependencies: <a name = "dependencies"></a>
NOTED: You need python installed already. If you don't have it, download it [here](https://www.python.org/downloads/)

- First of all, download the latest release [here](https://github.com/realandrinoff/TelegramHelpBot/releases)
<br>

- Then, unzip it anywhere you want.
- Head to the folder using terminal and typing <br>
```cd "PATH"``` (for example: ```cd Downloads/TelegramHelperBot```)
- When you are in the folder, type <br>
```python3 -m venv env```<br>
```pip install -r requirements.txt```

<h3>Congrats, you downloaded everything! 😚</h3>

---

## 🤖 Creating a bot: <a name = "creating"></a>

- On telegram go to the [BotFather](https://t.me/botfather)
- Type ```/newbot``` and enter data you want for your bot
<img src = "https://i.imgur.com/9412iSe.png">

<h3>That's that simple!</h3>

---

## 🔧 Configuring the bot (OPTIONAL): <a name = "config"></a>

You can also configure the bot to your liking. To see the options type ```/help```

<img src = "https://i.imgur.com/BN1oOZc.png">

---

## 🔧 Setting up virtual environment: <a name = "venv"></a>

Probably the hardest part so far. Virtual environment will help us save up storage, securely install all the dependencies and store the API keys.

To do so: 
- Go to your path (look [here](#-downloading-the-dependencies))
- We already have venv setup up, so we can type: <br>
```source env/bin/activate```

Now we are in the virtual environment. Next:

- You have to copy the API key:
<img src = "https://i.imgur.com/x7UoFsh.png">
- After you copied it go back to terminal.
- Type ```export TELEGRAM_TOKEN="PASTE_YOUR_TOKEN_HERE"``` (for example ```export TELEGRAM_TOKEN=12345C32D```)

That was step 1, now:
- Go to [@userinfobot](https://t.me/userinfobot) and send ```/start```![](https://i.imgur.com/vX9TYDs.png)
- Copy the Id and go back to terminal and type ```export YOUR_ID="PASTE_YOUR_ID_HERE"``` (for example ```export YOUR_ID=123456789)

<h3>🚩 That's almost it </h3>

---

## 🔧 Deploying: <a name = "deployment"></a>

Final step. In order for everything to work we have to deploy the project. To do so you can use your own computer. BUT the program has to be running in order for the bot to function. OR you can message [me](linktr.ee/andrinoff) to deploy it on my own server.

<h4>On your computer:</h4>

- In the same terminal type ```python3 app/main.py```

That's it! If you need help contact [me](linktr.ee/andrinoff)

---

## 🔧 Customizing: <a name = "customization"></a>

Go to ```/app/text``` folder. There you will find a file with all the text and example usage. You can customize it to your liking!

--- 

<h1>☕️ Thank you for staying through!</h1>