import emoji # type: ignore

x = input("Emoji: ")
print(emoji.emojize(f"Output: {x}", language="alias"))
