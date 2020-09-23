from time import time
'''
Name : Python Script to test your Typing Speed
Author : Ayushi Rawat

'''
 
print()
print("NO NEW LINE IS THERE, WRITE CONTINUOUSLY(just SPACES)")
s = "Roses are red, Violets are blue, The view is breathtaking, And so are you. "\
" Orchids are white,They grow in a pair, The sun is golden And so is your hair."\
"Sunflowers reach, Up to the skies, The ocean is cobalt, And so are your eyes."\
" Daisies are pretty, Tulips have style, My message is welcoming, And so is your smile."

words = (len(s.split()))
 
print()
print(s)
 
print("\nAfter you are done press enter to know your time and speed")
input("\nPress any key to Start:")
 
try:
    print("\nTimer Started\n")
    start = time()
    t = input()
    end = time()
    if t == s:
        total = round(end - start, 2)
        print("\nVoila you typed that correctly")
        print("Your time was %s seconds" % total)
        total = int(total) / 60        
        print("Speed was %s wpm" % (str(words // total)))
 
    else:
        print("\nWrongly entered")
        print("Try again")
 
except KeyboardInterrupt:
    print("")