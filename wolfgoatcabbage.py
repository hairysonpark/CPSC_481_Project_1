from search import *
# YOUR CODE GOES HERE


class WolfGoatCabbage(Problem):
    """The problem of transporting a [F]armer, [G]oat, [C]abbage, and [W]olf across a stream. W eats G, G eats C so these cannot be paired with 
     one another.  """

    def __init__(self, initial={'F', 'W', 'G', 'C'}, goal=set()):
        """Defining the goal state and initializing the problem"""
        super().__init__(initial, goal)

    def find_state(self, state):
        """Return the current state in a given state"""

        return state.copy(state)

    def actions(self, state):
        """Noting the various actions when crossing the river. """
        possible_actions = {'G', 'F'}, {'F'}, {'C', 'F'}, {'G', 'F'}, {'W', 'F'}, {
            'F'}, {'G', 'F'}, {'G', 'F'}, {'F'}, {'W', 'F'}, {'G', 'F'},
        {'C', 'F'}, {'F'}, {'G', 'F'}

        current_state = self.find_set(state)
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
    wgc = WolfGoatCabbage({'F', 'W', 'G', 'C'})
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
