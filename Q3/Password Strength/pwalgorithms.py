# Module pwalgorithms
import time

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("Q3/Password Strength/dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses
    
def two_words(password):
    words = get_dictionary()
    total_words = len(words)
    guesses = 0
    
    start_time = time.time()
    
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            guesses += 1
            combined_password = word1 + word2
            
            if combined_password == password:
                end_time = time.time()
                time_taken = end_time - start_time
                return True, guesses, time_taken
    
    end_time = time.time()
    time_taken = end_time - start_time
    return False, guesses, time_taken