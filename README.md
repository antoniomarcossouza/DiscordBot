# Discord Bot

I'm making a simple Discord bot for leaning purposes :)

As of now, what this bot does/offers?

- Automatic welcome/goodbye message when someone enters/leaves the server
- Commands for kicking, banning and banning temporarily
- Clear chat command
- Some TTRPG functions
  - Dice rolls in NdN format
  - Coinflips
  - D&D 5e Artificer 'Experimental Elixir' feature
  - A custom curse roll for a player character
- Play local audio files

What I intend to implement soon?

- Finish help command
- After tempban, bot PMs banned user with an invite to enter the server again
- Mute user messages
- Leveling system

## Installing instructions

- Install [Python](https://www.python.org/downloads/)
- Clone this repository with `git clone https://github.com/antoniomarcossouza/DiscordBot.git`
- To install all requirements, run `pip install -r requirements.txt`
- Duplicate the _.env.example_ file as _.env_ and change the values
- Execute with `python app.py`
