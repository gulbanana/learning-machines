# TODO: docs
# TODO: test

class Node:
    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.lowest_cost = cost

class Heap:
    def __init__(self):
        self.contents = []
        self.max = 0

    def insert(self, element):
        self.contents.append(element)
        if len(self.contents) > self.max:
            self.max = len(self.contents)

    def update_costs(self, state, cost):
        for node in self.contents:
            if node.state == state and node.lowest_cost > cost:
                node.lowest_cost = cost

    def extract_min(self):
        values = [node.lowest_cost for nodes in self.contents]
        idx = values.index(min(values))
        return self.contents.pop(idx)

class Ucs:
    def __init__(self, subject):
        self.subject = subject
        self.frontier = Heap()
        self.explored = []
        self.success_node = None

    def search(self):
        self.frontier.insert(Node(self.subject.current_state(), None))

        while self.frontier.contents:
            node = self.frontier.extract_min()
            self.explored.append(node)

            self.subject.set_state(node.state)

            if self.subject.current_state() == self.subject.goal_state():
                self.success_node = node
                return True

            self._add_next_states(node)

        return False

    def results(self):
        pass # TODO

    def _visited_nodes(self):
        return self.explored + self.frontier.contents or []

    def _add_next_states(self, parent):
        for state in self.subject.next_states():
            if [node.state for node in self._visited_nodes()].count(state) == 0:
                cost = self.subject.move_cost(self.subject.current_state(), state)
                self.frontier.insert(Node(state, parent, cost))
            elif [node.state for node in self.frontier.contents].count(state) == 1:
                cost = self.subject.move_cost(self.subject.current_state(), state)
                self.frontier.update_costs(state, cost)