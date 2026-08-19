import time
from javascript import require, On

mineflayer = require('mineflayer')

# CONFIGURATION
SERVER_IP = "eu.donutsmp.net" 
PORT = 25565                 

print("Starting Microsoft-Authenticated AFK Bot...")
bot = mineflayer.createBot({
    'host': SERVER_IP,
    'port': PORT,
    'auth': 'microsoft',             # Tells Mineflayer to use Microsoft Official Auth
    'username': 'your-email@outlook.com', # Use your official Microsoft Account Email
    'version': '1.21.1'
 
})

@On(bot, 'spawn')
def handle_spawn(*args):
    print("SUCCESS: Bot has joined the server using your Microsoft account!")
    while True:
        time.sleep(60)
        bot.setControlState('jump', True)
        time.sleep(0.5)
        bot.setControlState('jump', False)

@On(bot, 'kicked')
def handle_kick(this, reason, loggedIn, *args):
    print(f"Bot was kicked. Reason: {reason}")

# Keep script running
while True:
    time.sleep(1)
