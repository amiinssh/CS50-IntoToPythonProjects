def main():
    
    emoji_dict = {
        ":1st_place_medal:": "🥇",
        ":money_bag:": "💰",
        ":smile_cat:": "😸",
        ":thumbs_up:": "👍",
        ":thumbsup:": "👍",
        ":heart:": "❤️",
        ":fire:": "🔥",
        ":smiley:": "😃",
        ":sunglasses:": "😎",
        ":grin:": "😁",
        ":laughing:": "😂",
        ":cry:": "😢",
        ":angry:": "😠",
        ":sweat_smile:": "😅",
        ":blush:": "😊",
        ":wink:": "😉",
        ":confused:": "😕",
        ":thinking:": "🤔",
        ":relaxed:": "☺️",
        ":sleepy:": "😪",
        ":scream:": "😱",
        ":star_struck:": "🤩",
        ":zany_face:": "🤪",
        ":nerd_face:": "🤓",
        ":party_popper:": "🎉",
        ":clap:": "👏",
        ":sob:": "😭",
        ":trophy:": "🏆",
        ":rocket:": "🚀",
        ":earth_americas:": "🌎",
        ":sunny:": "☀️",
        ":umbrella:": "☔",
        ":cloud:": "☁️",
        ":snowflake:": "❄️",
        ":moon:": "🌕",
        ":star:": "⭐",
        ":sparkles:": "✨",
        ":balloon:": "🎈",
        ":gift:": "🎁"
    }

    user_input = input("Enter a string with emoji codes: ").strip()

    for code, emoji in emoji_dict.items():
        user_input = user_input.replace(code, emoji)

    print(f"Output: {user_input}")

if __name__ == "__main__":
    main()
