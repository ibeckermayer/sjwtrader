from model.Controversy import Controversy

class Category:
    """Class for storing Categories for analysis

    @param[in] category (str)                   : Name of the Category.
    """

    def __init__(self, category):
        """init for Controversy

        @param promisings (list[Controversy])   : List of promising Controversies belonging to Category.
        @param unpromisings (list[Controversy]) : List of unpromising Controversies belonging to Category.
        """
        self.category = category
        self.promisings = []
        self.unpromisings = []

    def add(self, controversy):
        """Adds a controversy to the Catgeroy

        @param[in] controversy: Controversy to be added
        """
        if controversy.is_promising:
            self.promisings.append(controversy)
        else:
            self.unpromisings.append(controversy)

    def num_controversies(self):
        """Returns the total number of controversies in this category
        """
        return len(self.promisings) + len(self.unpromisings)
