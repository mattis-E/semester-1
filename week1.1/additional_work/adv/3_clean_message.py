"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")
original = raw_message

# TODO: apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper
raw_message = raw_message.strip()
raw_message = raw_message.lower()
raw_message = raw_message.capitalize()

# TODO: display the original and cleaned messages
print(f"Original: {original}, character count: {original.count()}")
print(f"Cleaned: {raw_message}, character count: {raw_message.count()}")
# Extension: display the character counts for each version
