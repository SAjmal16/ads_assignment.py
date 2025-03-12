class MarksDistribution:
    """
    A class to represent the distribution of student marks.

    Attributes:
        _max (int): The highest value a mark can be (default 100).
        _min (int): The lowest value a mark can be (default 0).
        _marks (list of int): A list containing all student marks.
    """

    def __init__(self, max_mark=100, min_mark=0):
        """
        Initializes the MarksDistribution class with max and min mark values.

        Args:
            max_mark (int): The highest possible mark.
            min_mark (int): The lowest possible mark.

        Raises:
            ValueError: If max_mark is less than or equal to min_mark.
        """
        if max_mark <= min_mark:
            raise ValueError("Maximum mark must be greater than minimum mark.")
        self._max = max_mark
        self._min = min_mark
        self._marks = []

    def add_all(self, student_marks):
        """
        Adds a list of student marks to the _marks list.

        Args:
            student_marks (list of int): List of student marks.

        Raises:
            ValueError: If any mark is outside the allowed range.
        """
        if not all(self._min <= mark <= self._max for mark in student_marks):
            raise ValueError("All marks must be within the allowed range.")
        self._marks.extend(student_marks)

    def get_distribution(self, bins):
        """
        Generates a histogram distribution of marks into bins.

        Args:
            bins (int): Number of bins to group marks into.

        Returns:
            list of tuples: Each tuple contains a bin range label and the count of marks in that bin.

        Raises:
            ValueError: If the range of marks is not evenly divisible by the number of bins.
        """
        range_size = self._max - self._min
        if range_size % bins != 0:
            raise ValueError("The range of marks must be evenly divisible by the number of bins.")

        bin_size = range_size // bins
        distribution = {f"{i}-{i + bin_size - 1}": 0 for i in range(self._min, self._max, bin_size)}
        last_bin_label = f"{self._max - bin_size}-{self._max}"
        distribution[last_bin_label] = 0  # Ensuring the last bin includes max mark

        for mark in self._marks:
            for bin_start in range(self._min, self._max, bin_size):
                bin_end = bin_start + bin_size - 1
                if bin_start <= mark <= bin_end:
                    bin_label = f"{bin_start}-{bin_end}"
                    distribution[bin_label] += 1
                    break

        return list(distribution.items())


