"""
Emoji Enhanser for messages
"""

emoji_map_fun = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}

user_msg = input("Enter your msg: ")

updated_words = []

for word in user_msg.split():
    cleaned =  word.lower().strip(".,!?")
    emoji = emoji_map_fun.get(cleaned,"")
    if emoji:
        updated_words.append(f'{word} {emoji}')
    else:
        updated_words.append(word)


updated_msg = " ".join(updated_words)
print('\n Enhanched msssage:\n')
print(updated_msg)
