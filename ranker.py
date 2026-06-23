class Ranker:

    def rank(self, query_words, index):

        scores = {}

        for word in query_words:

            if word in index:

                docs = index[word]

                for doc, freq in docs.items():

                    if doc not in scores:
                        scores[doc] = 0

                    scores[doc] += freq

        results = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return results