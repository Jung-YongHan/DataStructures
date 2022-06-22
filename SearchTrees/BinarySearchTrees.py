class TreeMap(LinkedBinaryTree, MapBase):

    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key

        def value(self):
            return self.element()._value

    def subtree_search(self, p, k):
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self.subtree_search(self.left(p), k)
        elif k > p.key():
            if self.right(p) is not None:
                return self.subtree_search(self.right(p), k)
        return p

    def subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def subtree_last_position(self, p):
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError
        else:
            p = self.subtree_search(self.root(), k)
            self.rebalance_access(p)
            if k != p.key():
                raise KeyError
            return p.value()

    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self.add_root(self.Item(k, v))
        else:
            p = self.subtree_search(self.root(), k)
            if p.key == k:
                p.element().value = v
                self.rebalance_access(p)
                return
            else:
                item = self.Item(k,v)
                if p.key() < k:
                    leaf = self.add_right(p, item)
                else:
                    leaf = self.add_left(p. item)
        self.rebalance_insert(leaf)


