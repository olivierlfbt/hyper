from dataclasses import dataclass, field

@dataclass
class BlogPost:
    title: str
    content: str
    category: str
    todos: list = field(default_factory=list)
