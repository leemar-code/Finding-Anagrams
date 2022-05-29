def check(word, anagram):
    word = input("Enter the first word \n")
    anagram = input("Enter the second word \n")
   
    if sorted(word) == sorted(anagram):
        print("The words are anagram")
    else:
        print("The words are not anagram")

word = ""
anagram = ""
check(word, anagram)