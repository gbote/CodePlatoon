def bottle_song(n):
	# write your code here!
	if (n == 1):
		objects = 'bottle'
		objectsMinusOne = 'bottles'
	elif (n == 2):
		objects = 'bottles'
		objectsMinusOne = 'bottle'
	else:
		objects = 'bottles'
		objectsMinusOne = 'bottles'

	if (n > 0):
		print(f"{str(n)} {objects} of beer on the wall, {str(n)} {objects} of beer.")
		print(
		    f"Take one down and pass it around, {str(n-1)} {objectsMinusOne} of beer on the wall."
		)
	elif (n == 0):
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, 99 bottles of beer on the wall.")
	else:
		print("Error: Wheres the booze?")

for bottles in range(99, -1, -1):
	bottle_song(bottles)
