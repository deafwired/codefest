import os

from util.api import API


class QueryIndex:
    def generate_search(self, search, filename):
        api = API()
        results = {}

        with open(filename, "r") as file:
            for line in file:
                line = line.strip("\n")
                line = line.lower()
                split = line.split(",")
                file_path = split[0]
                file_path = os.path.basename(file_path)
                file_metadata = api.queryToKeywords(file_path)
                "".join(file_metadata)
                print(file_metadata)
                key_words = split[1:]

                for item in file_metadata:
                    key_words.append(item)

                print(key_words)

                score = sum(1 for word in search if word in key_words)  # Count matches

                if score > 0:  # Fix: Ensure at least one match
                    results[file_path] = score

            sorted_searches = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))  # Sort in descending order
            return sorted_searches


