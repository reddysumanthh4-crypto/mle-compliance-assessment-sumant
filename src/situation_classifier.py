class SituationClassifier:

    def classify(self, conversation):

        text = " ".join(
            msg["text"] for msg in conversation["messages"]
        ).lower()

        product_loss_keywords = [
            "never arrived",
            "never got",
            "never received",
            "refund",
            "charged after i cancelled"
        ]

        substandard_keywords = [
            "never worked",
            "didn't work",
            "bad service",
            "slow",
            "substandard"
        ]

        product_loss = any(k in text for k in product_loss_keywords)
        substandard = any(k in text for k in substandard_keywords)

        return {
            "conversation_id": conversation["conversation_id"],
            "product_loss": product_loss,
            "substandard_service": substandard,
            "other": not (product_loss or substandard)
        }