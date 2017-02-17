class Matrix:
	numberOfRows = 0
	numberOfColumns = 0
	content = [[0]]

	#Initializes the content variable with zeros
	def __init__(self, rows, columns):
		self.numberOfRows = rows
		self.numberOfColumns = columns
		self.content = [[0 for x in range(columns)] for x in range(rows)]
		for i in range(self.numberOfRows):
			for j in range(self.numberOfColumns):
				self.content[i][j] = 0

	def changeElement(self, rowNumber, columnNumber, value):
		self.content[rowNumber - 1][columnNumber - 1] = value

	def getTransposedMatrix(self):
		newMatrix = Matrix(self.numberOfColumns, self.numberOfRows)
		newMatrix.content = list(map(list, zip(*(self.content))))
		return newMatrix

	def getRow(self, rowNumber):
		return self.content[rowNumber - 1]

	#Takes a list and replaces a single row in the matrix with the contents of the list
	#The function automatically truncates or expands lists that aren't the corrent size
	def setRow(self, rowNumber, newRow):
		if len(newRow) == self.numberOfColumns:
			self.content[rowNumber - 1] = newRow
		elif len(newRow) > self.numberOfColumns:
			newRow = newRow[0:self.numberOfColumns]
			self.content[rowNumber - 1] = newRow
		else:
			while len(newRow) < self.numberOfColumns:
				newRow.append(0)
			self.content[rowNumber - 1] = newRow

	def getColumn(self, columnNumber):
		transposedMatrix = list(map(list, zip(*(self.content))))
		return transposedMatrix[columnNumber - 1]

	#Works the same way as the setRow() function except it transposes the matrix to perform the substituitions and then transposes it back
	def setColumn(self, columnNumber, newColumn):
		transposedMatrix = self.getTrasnposedMatrix()
		if len(newColumn) == self.numberOfColumns:
			transposedMatrix.content[columnNumber - 1] = newColumn
		elif len(newColumn) > self.numberOfColumns:
			newColumn = newColumn[0:self.numberOfColumns]
			transposedMatrix.content[columnNumber - 1] = newColumn
		else:
			while len(newColumn) < self.numberOfColumns:
				newColumn.append(0)
			transposedMatrix.content[columnNumber - 1] = newColumn

		self.content = transposedMatrix.getTrasnposedMatrix().content

	def scalarMultiplication(self, scalar):
		for i in range(self.numberOfRows):
			for j in range(self.numberOfColumns):
				self.content[i][j] = scalar * self.content[i][j]

	def getMatrix2DArray(self):
		return self.content
