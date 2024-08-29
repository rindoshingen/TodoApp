contents = ["All carrots are to be sliced longitudinally.",
			"The carrots were reportedly sliced horizontally.",
			"The carrots were presented properly."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
	file = open(f"../files/{filename}", 'w')
	file.write(content)
