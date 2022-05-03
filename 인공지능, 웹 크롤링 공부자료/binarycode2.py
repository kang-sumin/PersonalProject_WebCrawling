#Node 클래스에 노드값,오른쪽,왼쪽 노드 초기화
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinarySearchTree(object):
    #비어있는 이진트리로 초기화
    def __init__(self):
        self.root=None
    
    #삽입
    def insert(self, data):
        self.root=self.insert_value(self.root, data)
        return self.root is not None
    
    #값삽입
    def insert_value(self,node,data):
        if node==None:
            node=Node(data)
        else:
            if data<=node.data:
                node.left=self.insert_value(node.left, data)
            else:
                node.right=self.insert_value(node.right, data)
        return node
    
    #탐색
    def find(self, key):
        return self.find_value(self.root, key)
    
    #값탐색
    def find_value(self, root, key):
        if root==None or root.data==key:
            return root is not None
        elif key<root.data:
            return self.find_value(root.left, key)
        else:
            return self.find_value(root.right, key)
     
    #삭제
    def delete(self, key):
        self.root=self.delete_value(self.root, key)
        deleted=self.delete_value(self.root, key)
        return deleted
    
    #값삭제
    def delete_value(self, node, key):
        if node==None:
            return node, False
        
        deleted=False
        if (key == node.data):
            deleted=True
            if node.left and node.right:
                parent, child=node, node.right
                while child.left is not None:
                    parent, child=child, child.left
                child.left=node.left
                if parent !=node:
                    parent.left=child.right
                    child.right=node.right
                node=child
            elif node.left or node.right:
                node=node.left or node.right
            else:
                node=None
        elif key<node.data:
            node.left, deleted=self.delete_value(node.left, key)
        else:
            node.right, deleted=self.delete_value(node.right, key)
        return node, deleted
    
    
    
    
#main
array=[40,4,34,45,14,55,48,13,15,49,47]

bst=BinarySearchTree()

for x in array:
    bst.insert(x)
#find   
print(bst.find(15)) #true
print(bst.find(17)) #false
#delete
print(bst.delete(55)) #true
print(bst.delete(14)) #true
print(bst.delete(11)) #false