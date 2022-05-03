#BinaryTree 클래스
class BinaryTree:
    def __init__(self):
        self.rootNode=None
            
    def add(self, data):
        current=self.rootNode
        newNode=self.Node(data) #노드를 추가하면 데이터를 받아 Node class로 이동
        
        if(self.rootNode==None):
            self.rootNode=newNode
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
            
    #중위탐색 출력함
    def print_inorder(self):
        self.inorder(self.rootNode)
    
    #preorder traversal 전위순회    
    def preorder(self, node):
        if(node==None):
            return
        print(node.data)
        self.inorder(node.left)
        self.inorder(node.right)
        
    #inorder traversal 중위순회
    def inorder(self, node):
        if(node==None):
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)
    
    #postorder traversal 후위순회
    def postorder(self, node):
        if(node==None):
            return
        self.inorder(node.left)
        self.inorder(node.right)
        print(node.data)
        
    
    #노드를 초기화해서 생성하는 클래스
    class Node:
        def __init__(self, data):
             self.data=data
             self.left=None
             self.right=None
            
             
#main
array=[40,48,56,825,51,22,46]

bt=BinaryTree()
for x in array:
    bt.add(x)

'''
bt.add('kim')
bt.add('lee')
bt.add('kang')
'''
bt.print_inorder()

