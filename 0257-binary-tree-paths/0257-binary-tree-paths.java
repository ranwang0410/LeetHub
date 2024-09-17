/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
       List<String> s=new ArrayList<>();
     String ss="";
     helper(root,s,ss);
    return s;
    }
    public static void helper(TreeNode root , List<String> s,String ss)
    {   
        if(root==null)
        {return ;}
        if(root.left==null && root.right==null)
        {
            ss+=root.val;
            s.add(ss);
            ss="";
            return ;
        }
        ss+=root.val+"->";
        helper(root.left,s,ss);
        helper(root.right,s,ss);
    }
}