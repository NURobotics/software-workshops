#!/usr/bin/env python

if __name__ == '__main__':
  english_lang = [8.167, 1.492, 2.782, 4.243, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, \
                  6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
  
  f = open('encrypted.txt','r').read()
  freq = [0.0]*26
  for c in f:
    index = ord(c.lower()) - 97
    if index >= 0 and index < 26:
      freq[index] += 1.0
  total_count = sum(freq)
  for index, count in enumerate(freq): freq[index] /= total_count
  
  costs = [0.0]*26
  min_cost = float("inf")
  min_shift = 0
  for shift in range(26):
    cost = 0.0
    for letter_index, letter_freq in enumerate(english_lang):
      cost += (freq[(shift + letter_index)%26]-english_lang[letter_index])**2
    if cost < min_cost:
      min_cost = cost
      min_shift = shift
    costs[shift] = cost
  
  out = open('decrypted.txt','w')
  remake = ''
  for s in f:
    index = ord(s)
    if index >= 97 and index <= 122: 
      remake += chr(((index-97-min_shift)%26)+97)
    elif index >= 65 and index <= 90:
      remake += chr(((index-65-min_shift)%26)+65)
    else:
      remake += s
  out.write(remake)
  out.close()
 
  print
  print 'The encryption key was found to be %d\n\n' % min_shift
  print 'Original:\n'
  print f
  print
  print 'Decrypted:\n'
  print remake
  
