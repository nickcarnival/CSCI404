class Tree():
    """
    This tree will hold a source node, and the paths that it has available
    """
    paths = [{'Names' : 'Weights'}]
    # create it with the source node and no children
    def __init__(self, source):
        self.source = source

    # add child to the path where it belongs and adjust that paths weight
    def add_child(self, child, weight, source):
        # paths['Bremen'].append({})
        print(self.paths)
        self.paths[source].append({child : weight})
