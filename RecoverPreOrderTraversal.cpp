/*
Leetcode 1028 - Recover a Tree From Preorder Traversal
Given a string, we need to create a Pre-order traversal Binary Tree using DFS.
*/
class Solution {
public:
    TreeNode* recoverFromPreorder(string traversal) {
        stack<TreeNode*> st;
        int i = 0, n = traversal.size();
        while (i<n){
            int depth = 0;
          // calculate depth
            while (i<n && traversal[i] == '-'){
                depth++;
                i++;
            };

            int num = 0;
          // for multidigit numbers
            while (i < n && isdigit(traversal[i])) {\
                num = num * 10 + (traversal[i] - '0');  
                i++;
            };

          // Create new node
            TreeNode* node = new TreeNode(num);
          // Left child
            if (depth == st.size()) {
                if (!st.empty()) {
                    st.top()->left = node;
                }
            } else {
              // Right child
                while (st.size() > depth) {
                    st.pop();
                }
                if (!st.empty()) {
                    st.top()->right = node;
                }
            }
          // Add node to stack
            st.push(node);
        };
      // Remove objects in stack except root
        while (st.size() > 1) {
            st.pop();
        }
        return st.top();
    };
};
