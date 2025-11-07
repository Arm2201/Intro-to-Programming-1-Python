print('Hello World!')
print('I am changing this file as well.')



word = """[Intro]
Desert you
Ooh-ooh-ooh-ooh
Hurt you

[Verse 1]
We're no strangers to love
You know the rules and so do I (Do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Verse 2]
We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it
See Rick Astley Live
Get tickets as low as $79
You might also like
So Long, London
Taylor Swift
loml
Taylor Swift
THE HEART PART 6
Drake
[Pre-Chorus]
And if you ask me how I'm feeling
Don't tell me you're too blind to see

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Bridge]
Ooh (Give you up)
Ooh-ooh (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
[Verse 3]
We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
"""

count = word.lower().count("never gonna")
print("1.",count)


lines = word.split("\n")
remove_section = []

for line in lines:
    if not (line.startswith("[") and line.endswith("]")):
        remove_section.append(line)

clean_lyrics = "\n".join(remove_section)
print("2.",clean_lyrics)


count = 0
for line in lines:
    if not (line.startswith("[") and line.endswith("]")):
        count += 1

print("3.", count)


total_letters = 0

for line in lines:
    if not (line.startswith("[") and line.endswith("]")):
        for char in line:
            if char.isalpha():  # counts only letters (a-z, A-Z)
                total_letters += 1

print("4.", total_letters)