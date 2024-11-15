# code = "sami ullah baig"
# modified_code = ' '.join([word[1:] + word[0] for word in code.split()])

# print(modified_code)

# if (len(code) == 3):
#     print(code[::-1])

# Ask the user whether they want to encode or decode
mode = input("Do you want to encode or decode? ").strip().lower()
message = input("Enter the message: ").strip()
processed_words = []
words = message.split()
for word in words:
    if mode == "encode":
        if len(word) >= 3:
            modified_word = word[1:] + word[0]
            random_chars = 'abc'
            processed_word = random_chars + modified_word + random_chars
        else:
            processed_word = word[::-1]
    elif mode == "decode":
        if len(word) < 3:
            processed_word = word[::-1]
        else:
            modified_word = word[3:-3]
            processed_word = modified_word[-1] + modified_word[:-1]
    else:
        print("Invalid mode selected.")
        break
    processed_words.append(processed_word)
result = ' '.join(processed_words)
print("Result:", result)
 