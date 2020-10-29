#socks-warm up challanges
'''li=[int(x)for x in input().split(' ')]
temp=[]
c=0
for e in li:
	if e not in temp:
		a=(li.count(e))//2
		c=c+a
		temp.append(e)
print(c)

'''
s = input()
n = int(input())
segment_length = len(s)
print("sl",segment_length)
segment_count = s.count("a")
print("sc",segment_count)
ratio = n // segment_length
print("r",ratio)
remainder = segment_length - n % segment_length
print("rem",remainder)
first_segments_count = ratio * segment_count
print("fsc",first_segments_count)
last_partial_segment_count = s.count("a", 0, segment_length - remainder)
result = first_segments_count + last_partial_segment_count
print(result)