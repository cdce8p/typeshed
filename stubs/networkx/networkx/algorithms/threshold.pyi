from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["is_threshold_graph", "find_threshold_graph"]

@_dispatchable
def is_threshold_graph(G: Graph[_Node]): ...
@_dispatchable
def find_threshold_graph(G: Graph[_Node], create_using: Graph[_Node] | None = None): ...
