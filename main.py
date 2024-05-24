import string

letters = string.ascii_letters
user_text = input("Enter letters in format: 'a-c' ").strip()
if len(user_text) == 3 and user_text[0].isalpha() and user_text[1] == "-" and user_text[2].isalpha():
    first_letter = user_text[0]
    second_letter = user_text[2]
    start_index = letters.find(first_letter)
    end_index = letters.find(second_letter)

    if start_index > end_index + 1:
        start_index, second_index = second_index, start_index
    print(letters[start_index:end_index+1])
else:
    print("Invalid format!")





