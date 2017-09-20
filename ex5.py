s = "Hi there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurence of "a" should be at index 8
print("the first occurence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("the first five characters are '%s'" % s[:5])     # starts to 5
print("the next five characters are '%s'" % s[5:10])    # 5 to 10
print("the thirteenth character is '%s'" % s[12])       # just number 12
print("the characters with odd index are '%s'" % s[1::2])   # zero-based index
print("the last five characters are '%s'" % s[-5:]) # fifth-from-last-to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
