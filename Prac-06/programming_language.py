class ProgrammingLanguage:
    """Represents a Programming language object."""

    def __init__(self, name, types, reflection, year):
        """Initialises the Programming language instance"""
        self.name = name
        self.type = types
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if Programming language is dynamically typed."""
        return self.type == "Dynamic"

    def __str__(self):
        """Returns the Programming language object as a string"""
        return "{}, {}, reflection={}, appeared in year {}".format(self.name, self.type,
                                                                   self.reflection, self.year)
