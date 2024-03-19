#characterFrequency

string_freq = "HelloWorld"
dic_freq = {}

for i in string_freq:
    if i  in dic_freq:
        dic_freq[i] += 1
    else:
        dic_freq[i] = 1

print("Character frequency:\n "+ str(dic_freq))