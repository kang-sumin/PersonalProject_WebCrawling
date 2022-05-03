
class BinaryTree:
    def __init__(self):
        self.rootNode=None
            
    def add(self,data):
        newNode=self.Node(data)
        current=self.rootNode
        
        if(self.rootNode==None):
            rootNode=newNode
            return
        
        while(current!=None):
            parent=current
            if(current.data<newNode.data):
                compare=1
                current=current.right
            else:
                compare=0
                current=current.left
        if(compare==1):
            parent.right=newNode
        else:
            parent.left=newNode
            
    def print_inorder(self):
        self.inorder(self.rootNode)
        
    def inorder(self, node):
        if(node==None):
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)
        
     class Node:
        def __inti__(self,data):
            self.data=data
            self.left=None
            self.right=None
            
        
        
 
    
#main
bt=BinaryTree()

