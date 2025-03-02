class QueryIndex:
    def generate_index(self, filename):
        index = {}

        with open(filename, "r") as file:
            for line in file:
                line = line.strip("\n")
                split = line.split(",")
                file_path = split[0]
                keywords = split[1:]
                index[file_path] = keywords
        print(index)
