class node:
	def __init__(self, cNum, mdNum):
		self.cNum = cNum
		self.mdNum = mdNum
		self.metaData = []
		self.children = []
def main():
	with open('input08.txt', 'r') as puzzleInput:
		input = puzzleInput.readline().split()
		root = node(1, 0)
		buildTree(root, input)
		print(f"Part 1: {metaDataSum(root)}")
		print(f"Part 2: {nodeValue(root.children[0])}")

def buildTree(root, input):
	newNode = node(int(input.pop(0)), int(input.pop(0)))
	root.children.append(newNode)
	for _ in range(newNode.cNum):
		buildTree(newNode, input)
	for _ in range(newNode.mdNum):
		newNode.metaData.append(int(input.pop(0)))
def metaDataSum(root):
	result = 0
	for i in root.children:
		result += metaDataSum(i)
	for i in root.metaData:
		result += i
	return result
def nodeValue(root):
	result = 0
	if root.cNum == 0:
		for i in root.metaData:
			result += i
	else:
		for i in root.metaData:
			if i <= len(root.children):
				result += nodeValue(root.children[i - 1])
	return result

main()