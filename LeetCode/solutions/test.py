def mergeTrees(root1, root2):
        root1 = [0 if root1[i] == None else root1[i] for i in range(len(root1))]
        root2 = [0 if root2[i] == None else root2[i] for i in range(len(root2))]
        

        longer_root, shorter_root = root1,root2
        if len(root2)>len(root1):
            longer_root, shorter_root = root2, root1
        
        for i in range(len(longer_root)-len(shorter_root)):
            shorter_root.append(0)
            
        # merged_root = []
        # for i in range(len(longer_root)):
        #     merged_root.append(shorter_root[i]+longer_root[i])
            
        merged_root = [shorter_root[i]+longer_root[i] for i in range(len(longer_root))]
        
        return merged_root

root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]

result = mergeTrees(root1,root2)

print(result)