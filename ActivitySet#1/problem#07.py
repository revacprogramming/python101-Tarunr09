# Strings

text = "X-DSPAM-Confidence: 0.8475"
pos = text.find('0.8475')
a=float(text[pos:])
print(a)
