//2 3 4 5 6
//so nextInt() 2 dega ?yes or no
//yessss
//next "2" dega
//nextline "2 3 4 5 6" dega
//so nextInt()
//if 
//piyush deepa deeyush aise aarha 
//i want them individually'
//s.next() ok



//insertion
import java.util.*;
class Node
{
int data;
Node left,right;

Node(int key)
{
data=key;
left=right=null;
}
}//node
class BST
{
public static Node insert(Node root,int key){
if(root==null)
{  return new Node(key);
}
if(key>root.data){
root.right=insert(root.right,key);
}
else
{
root.left=insert(root.left,key);
}
return root;

}

public static void inorder(Node root)
{
if(root ==null)
return;
inorder(root.left);
System.out.print(root.data+" ");
inorder(root.right);
}
public static void main(String args[])
{	Node root=null;
	// number of node bhi
//1 2 3 4 5 6 aise dega user haan
	Scanner s = new Scanner(System.in);	
	//System.out.println("Enter the number of nodes");
	int n = s.nextInt();
		int [] keys = new int[n];
	for(int i =0;i<n;i++)
		keys[i] = s.nextInt();
for(int key:keys)
{
	root=insert(root,key);
}
inorder(root);
}

}//class bst