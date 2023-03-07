from search import *
# YOUR CODE GOES HERE


class WolfGoatCabbage(Problem):
    """The problem of transporting a [F]armer, [G]oat, [C]abbage, and [W]olf across a stream. W eats G, G eats C so these cannot be paired with 
     one another.  """

    def __init__(self, initial, goal=[[{'G', 'F'}, {'F'}, {'W', 'F'}, {'G', 'F'}, {'C', 'F'}, {'F'}, {'G', 'F'}],
                                      [{'G', 'F'}, {'F'}, {'C', 'F'}, {'G', 'F'}, {'W', 'F'}, {'F'}, {'G', 'F'}]]):
        """Defining the goal state and initializing the problem"""
        super().__init__(initial, goal)

    def actions(self, state):
        """Noting the various pairs when crossing the river. """
        possible_pairs = [{''}]
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
