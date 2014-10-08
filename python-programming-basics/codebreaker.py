#!/usr/bin/env python

if __name__ == '__main__':
  english_lang = [8.167, 1.492, 2.782, 4.243, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
  f = open('encrypted.txt','r').read()
  count = [0]*26
  total_count = 0.0
  for c in f:
    index = ord(c.lower()) - 97
    if index >= 0 and index < 26:
      count[index] += 1
      total_count += 1
  
  cost = []
  min_cost = float("inf")
  min_shift = 0
  for shift in range(26):
    diff = 0.0
    for f_index, freq in enumerate(english_lang):
      diff += ((count[(shift + f_index)%len(english_lang)]/total_count)-english_lang[f_index])**2
    diff**0.5
    if diff < min_cost:
      min_cost = diff
      min_shift = shift
    cost.append(diff)
  out = open('decrypted.txt','w')
  remake = ''
  for s in f:
    index = ord(s.lower()) - 97
    if index >= 0 and index < 26:
      remake += chr(((ord(s.lower())-97-min_shift)%26)+97)
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
  
