from matrixclass import Matrix

#########################################

def MatrixProduct(matrixA, matrixB):
	if matrixA.numberOfColumns == matrixB.numberOfRows:
		resultantMatrix = Matrix(matrixA.numberOfRows, matrixB.numberOfColumns)
		matrixBT = matrixB.getTrasnposedMatrix()
		resultantPointer = [1, 1]
		sum = 0
		for rowA in matrixA.getMatrix2DArray():
			resultantPointer[1] = 1
			for rowB in matrixBT.getMatrix2DArray():
				for i in range(matrixA.numberOfColumns):
					sum += rowA[i]*rowB[i]
				resultantMatrix.changeElement(resultantPointer[0], resultantPointer[1], sum)
				sum = 0
				resultantPointer[1] += 1
			resultantPointer[0] += 1
		return resultantMatrix
	else:
		raise NameError("These matrices cannot be multiplied")

#########################################

def main():
	testMatrixA = Matrix(2, 3)
	testMatrixA.setRow(1, [1,3,0])
	testMatrixA.setRow(2, [4,1,0])

	testMatrixB = Matrix(3, 3)
	testMatrixB.setRow(1, [0,0,1])
	testMatrixB.setRow(2, [0,1,0])
	testMatrixB.setRow(3, [1,0,0])
	
	result = MatrixProduct(testMatrixA, testMatrixB)
	print(result.getMatrix2DArray())
	
	return 0

#########################################

if __name__ == "__main__":
	main()
