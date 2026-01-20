def to_upper(text):
    return text.upper()
def to_lower(text):
    return text.lower()
def reverse_string(text):
    return text[::-1]
def count_characters(text):
    return len(text)
def is_palindrome(text):
    cleaned =  text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]