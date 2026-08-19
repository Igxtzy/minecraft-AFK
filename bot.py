import time
from javascript import require, On

mineflayer = require('mineflayer')

# ====================== CONFIG ======================
SERVER_IP = "eu.donutsmp.net"
PORT = 25565
VERSION = "1.21.1"          # change if the server uses a different version
EMAIL = "your-email@outlook.com"   # put real email here or better: use env var
# ====================================================

print("Starting Microsoft-Authenticated AFK Bot...")

bot = mineflayer.createBot({
    'host': SERVER_IP,
    'port': PORT,
    'auth': 'microsoft',
    'username': EMAIL,
    'version': VERSION,
    'checkTimeoutInterval': 60_000,   # helps with random disconnects
    'hideErrors': False
})

@On(bot, 'login')
def on_login(*args):
    print("Logged in successfully")

@On(bot, 'spawn')
def on_spawn(*args):
    print("SUCCESS: Bot has spawned on the server!")
    # simple AFK jump loop (runs in background via JS event loop)
    def jump_loop():
        while True:
            try:
                bot.setControlState('jump', True)
                time.sleep(0.4)
                bot.setControlState('jump', False)
                time.sleep(55)          # jump every \~55 seconds
            except Exception as e:
                print("Jump error:", e)
                time.sleep(5)

    # start the jump loop in a separate thread so it doesn't block
    import threading
    t = threading.Thread(target=jump_loop, daemon=True)
    t.start()

@On(bot, 'kicked')
def on_kicked(this, reason, logged_in, *args):
    print(f"Kicked! Reason: {reason}")

@On(bot, 'error')
def on_error(this, err, *args):
    print("Bot error:", err)

@On(bot, 'end')
def on_end(this, reason, *args):
    print("Connection ended:", reason)

# Keep the Python process alive
print("Bot is running... (Ctrl+C to stop)")
while True:
    time.sleep(1)