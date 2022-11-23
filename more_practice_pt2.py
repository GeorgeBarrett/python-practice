# importing another py file
import more_practice

# storing a sentence in a variable called sentence 
sentence = 'All good things come to those who wait.'


words = more_practice.break_words(sentence)
words
sorted_words = more_practice.sort_words(words)
sorted_words
more_practice.print_first_word(words)
more_practice.print_last_word(words)
words
more_practice.print_first_word(sorted_words)
more_practice.print_last_word(sorted_words)
sorted_words
sorted_words = more_practice.sort_sentence(sentence)
sorted_words
more_practice.print_first_and_last(sentence)
more_practice.print_first_and_last_sentence_sorted(sentence)