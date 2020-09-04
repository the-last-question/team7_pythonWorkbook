def displayVerse(n):
	print("One the "+n+ "day of christmas")
	print("my true love sent to me:")
	if(n>=12):
		print("Twelve drummers drumming,")
	if(n>=11):
		print("eleve pipers piping,")
	if(n>=10):
		print("ten lods a leaping",)
	if(n>=9):
		print("nine laids dancing,")
	if(n>=8):
		print("eight maids a milking,")
	if(n>=7):
		print("seven swans a swimming,")
	if(n>=6):
		print("six geese a laying,")
	if(n>=5):
		print("five golden rings,")
	if(n>=4):
		print("four calling birds,")
	if(n>=3):
		print("three french hens,")
	if(n>=2):
		print("two turtle doves,")
	if(n==1):
		print("A", end=" ")
	else:
		print("and a", end=" ")
	print("partridge in a pear tree.")
	print()
def main():
	for verse in range(1, 13):
		displayVerse(verse)
main()