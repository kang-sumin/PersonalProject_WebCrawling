class HuffmanTree:
    
    def __init__(self, dicData):
        self.nodes=[]
        for key in dicData.keys():
            self.nodes.append(self.Node(key,dicData[key]))
        
            
        self.makeTree()
        node=self.nodes[0].left.right.right
        print(node.ch," : ", node.count)
    
    
    def makeTree(self):
        while(len(self.nodes)>1):
            first=self.getMinNode()
            second=self.getMinNode()
            newNode=self.Node(None,first.count+second.count)
            newNode.left=first
            newNode.right=second
            self.nodes.append(newNode)
        

    def getMinNode(self):
        minNode=self.nodes[0]
        for i in range(1,len(self.nodes)):
            if(minNode.count>self.nodes[i].count):
                minNode=self.nodes[i]
        return self.nodes.pop(self.nodes.index(minNode))
        
            
    
    
    class Node:
        def __init__(self, ch, count):
            self.ch=ch
            self.count=count
            self.left=None
            self.right=None
            
            
            
            
            
            
#main
dicData={'a':5, 'b':3, 'c':2, 'd':7, 'e':10}
bitdicData={'a':00,'b':011,'c':010,'d':10}

huffman=HuffmanTree(dicData)
bithuffman=HuffmanTree(bitdicData)
