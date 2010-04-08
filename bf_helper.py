class Memory_Cell:
    def __init__(self):
        self.value = 0

        # We use this value when printing the whole Memory
        self.visited = False

    def __str__(self):
        return "%s" % self.value

    def inc_value(self):
        if self.value <= 255:
            self.value += 1

    def dec_value(self):
        if self.value > 0:
            self.value -= 1

    def set_value(self, value):
        # A cell should only hold values between 0 and 255
        if self.value >= 0 and self.value <= 255:
            self.value = value
        else:
            return -1

    def set_visited(self):
        self.visited = True

    def is_visited(self):
        return self.visited

class Memory:
    def __init__(self, size=200):
        # Index of the current cell
        self.pointer = 0

        self.array = []

        for k in range(size):
            self.array.append(Memory_Cell())

        # Make the first cell visited
        self.array[self.pointer].set_visited()

    def print_array(self):
        counter = 0
        for cell in self.array:
            if cell.is_visited():
                # Indicate where we are
                if counter == self.pointer:
                    print "[%s]: %s \"%s\" <-- PTR" % (counter, cell.value,
                            chr(cell.value))
                else:
                    print "[%s]: %s \"%s\"" % (counter, cell.value,
                            chr(cell.value))
                counter += 1

            # There should be nothing more ahead that's activated
            else:
                print "[%s]: END OF ARRAY" % counter
                break

    def inc_pointer(self):
        if self.pointer == len(self.array):
            return -1 # Already at limit

        self.pointer += 1

        # Activate the cell
        self.array[self.pointer].set_visited()

        return self.pointer

    def dec_pointer(self):
        if self.pointer == 0:
            return -1 # Already at limit

        self.pointer -= 1

        return self.pointer

    def inc_value(self):
        self.array[self.pointer].inc_value()

        return self.array[self.pointer].value

    def dec_value(self):
        self.array[self.pointer].dec_value()

        return self.array[self.pointer].value

    def output_value(self):
        print chr(self.array[self.pointer].value)

    def input_char(self, char):
        self.array[self.pointer].set_value(ord(char))

    def get_value(self):
        return self.array[self.pointer].value

memory_array = Memory()
valid_chars = ["+", "-", ">", "<", ",", ".", "[", "]"]

def parse_string(str_input):
    if str_input == "p":
        memory_array.print_array()
    elif str_input == "q":
        return 1
    else:
        while len(str_input):
            char = str_input[0]
            if char in valid_chars:
                if char == "+":
                    memory_array.inc_value()
                elif char == "-":
                    memory_array.dec_value()
                elif char == ">":
                    memory_array.inc_pointer()
                elif char == "<":
                    memory_array.dec_pointer()
                elif char == ",":
                    str_value = raw_input("Value for cell %s> " % memory_array.pointer)
                    memory_array.input_char(str_value)
                elif char == ".":
                    memory_array.output_value()
                elif char == "[":
                    while memory_array.get_value() != 0:
                        # To make a loop, se first have to find
                        # the matching ]
                        index_param = str_input.find("]")

                        # Pass the contents of the loop body
                        # Note: We remove the "[" and "]"
                        loop_body = str_input[1:index_param]
                        parse_string(loop_body)

                    # We still need to keep the "]" here, so it can be
                    # removed at the and of this loop
                    str_input = str_input[str_input.find("]"):]

            str_input = str_input[1:]


def main_loop():
    memory_array = Memory()
    valid_chars = ["+", "-", ">", "<", ",", ".", "[", "]"]

    while True:
        str_input = raw_input("Prompt> ")
        result = parse_string(str_input)

        if result == 1:
            break


if __name__ == "__main__":
    main_loop()
