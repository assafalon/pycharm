__author__ = 'assafalon'
# get a sting s as input
s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
# split string into a list of words
word_list = s.split()
# initiate a word dictionary
dic = {}
for word in word_list:
    dic[word]=0

for word in word_list:
    if not dic[word]:
        dic[word]=1
    else:
        dic[word]+=1

for key, value in dic.iteritems():
    print key, value