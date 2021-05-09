import pandas as pd
 from mainParserMagnolia import parser

 def RUN():
 	global parser
	
	del parser['Name'][len(parser['Name']) - 1]

	parser = pd.DataFrame(parser)

 	for step in range(len(parser)):
 		if list(parser['Name']).count(parser['Name'][step]) > 1:
 			parser.drop(step, inplace=True)
		

 	parser.to_csv("Magnolia.csv", index=None)


if __name__ == "__main__":
	RUN()
	
	df = pd.read_csv("Magnolia.csv")
	# print(list(df['Measure']))

	df = df.replace('<span class="price_measure">/шт</span>', "/шт")
	df = df.replace('<span class="price_measure">/кг</span>', "/кг")

	df.to_csv("Magnolia.csv", index=None)
