#You have to read this file in your python program and find out words with maximum occurance.
word_stats={}
with open (r'C:\\Users\\SESA610197\\Documents\\AIMLLNG\\Python Learning\\Read, Write Practice\\Read , Write Practice.txt', "r") as f:
    for line in f:
      words=line.split(' ')
      for word in words:
        if word in word_stats:
          word_stats[word]+=1
        else:
          word_stats[word] = 1

print(word_stats)

word_occurances = list(word_stats.values())
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_stats.items():
    if count==max_count:
        print(word)
        
    

        
