import os
from telegram import Bot

# Ganti dengan token bot Telegram Anda
TELEGRAM_BOT_TOKEN = "7619947662:AAHPlW2JCyOMz4aKmr_LKpNLWRG4FGFlf14"
# Ganti dengan chat ID Telegram Anda
TELEGRAM_CHAT_ID = "-1002337280272"

# Membuat objek bot dengan token
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Direktori tempat file disimpan
downloads_dir = "./downloads/"

# Loop untuk mengupload semua file di folder ./downloads/
for file_name in os.listdir(downloads_dir):
    file_path = os.path.join(downloads_dir, file_name)

    # Periksa apakah file tersebut adalah file biasa dan bukan direktori
    if os.path.isfile(file_path):
        print(f"Mengupload file: {file_name}")
        
        # Kirim file ke Telegram
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id=TELEGRAM_CHAT_ID, document=file)
        
        print(f"Berhasil mengupload: {file_name}")
    else:
        print(f"{file_name} bukan file yang valid.")
