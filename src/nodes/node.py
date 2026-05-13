from ..civilization.events import Event, EventType

__all__ = ["Node"]

class Node:
    """
    Basic Node class

    This will allow you to create a node (human) to live in your
    civilization!
    """
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.age: int = 0
        self.job: str | None = None
        self.moral: int = 85
        self.influence: int = 1
        self.likes: dict[str, Node] = {}
        self.dislikes: dict[str, Node] = {}

    # Set / Change / Update
    #region
    def increment_age(self) -> None:
        """Increase the age of the current node"""
        self.age += 1

    def change_job(self, new_job) -> None:
        """Change the job of the current node"""
        self.job = new_job

    def change_influence(self, new_level: int) -> None:
        """Change the influence level of a node"""
        self.influence = new_level

    def change_moral(self, addition: int) -> None:
        """Add / subtract moral from the current node"""
        self.moral += addition

    def add_like(self, node: "Node") -> None:
        """
        Add a liked node to the current node

        Will remove the node from self.dislikes
        """
        if node.name in self.dislikes:
            del self.dislikes[node.name]
        self.likes[node.name] = node

    def add_dislike(self, node: "Node") -> None:
        """
        Add a disliked node to the current node

        Will remove the node in self.likes if found
        """
        if node.name in self.likes:
            del self.likes[node.name]
        self.dislikes[node.name] = node
    #endregion

    # Events
    #region
    def on_event(self, event: Event) -> None:
        """Run an event for the current node"""
        match event.type:
            case EventType.INCREASE_AGE:
                self.increment_age()
    #endregion

    # Display (Getting)
    #region
    def __str__(self) -> str:
        return f"Node {self.name}"

    def get_moral(self) -> str:
        """
        Get the moral of a Node

        Returns Great, Good, Neutral, Poor
        """
        return (
            "Great" if self.moral >= 90 else
            "Good" if self.moral >= 75 else
            "Neutral" if self.moral >= 65 else
            "Poor"
        )

    def get_likes(self) -> dict[str, "Node"]:
        """
        Get a dict of all the liked nodes
        """
        return self.likes

    def get_dislikes(self) -> dict[str, "Node"]:
        """
        Get a dict of all the disliked nodes
        """
        return self.dislikes
    #endregion
