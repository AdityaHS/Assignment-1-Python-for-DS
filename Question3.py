def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    return result


input_sentence = str(input("Enter a string : "))
output_sentence = capitalize_words(input_sentence)
print(output_sentence)