/*
Leetcode 1261 - Find elements in a contaminated binary tree
We're given a binary tree that has this kind of structure:
-1
 \
  -1

Root is the top which equals to -1, Left = Null, Right = -1
We need to recover this binary tree by 1. Resetting root->val to 0 and then indexing the childs by 1 from left to right (bfs)
the values of left are odd and the values of right are even thus left=2x+1 and right=2x+2 (+2 because when x = 0, right = 2)
We can generate the map via a recursion and at each recursion, we append the index into a hashmap/set
To find the target we just search the map/set for said value and boom.
*/ 

#include <iostream>
#include <unordered_set>

struct Root
{
    int val;
    Root *left;
    Root *right;
    Root(int x) : val(x), left(NULL), right(NULL) {}
};

class BinaryTree
{
public:
    std::unordered_set<int> map;

    BinaryTree(Root *r)
    {
        if (r != nullptr)
        {
            r->val = 0;
            generateTree(r);
        }
    }

    bool find(int target)
    {
        return map.find(target) != map.end();
    }

private:
    void generateTree(Root *r)
    {
        if (r == NULL)
            return;

        map.insert(r->val);

        if (r->left != NULL)
        {
            r->left->val = (2 * r->val) + 1;
            generateTree(r->left);
        }
        if (r->right != NULL)
        {
            r->right->val = (2 * r->val) + 2;
            generateTree(r->right);
        }
    }
};

int main()
{

    Root *r = new Root(-1);
    r->right = new Root(-1);

    BinaryTree bt(r);

    std::cout << std::boolalpha;
    std::cout << "Find 0: " << bt.find(0) << "\n";
    std::cout << "Find 1: " << bt.find(1) << "\n";
    std::cout << "Find 2: " << bt.find(2) << "\n";
    std::cout << "Find 3: " << bt.find(3) << "\n";

    return 0;
}
