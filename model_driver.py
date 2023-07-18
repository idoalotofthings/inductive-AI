from transformers import AutoTokenizer, AutoModelWithLMHead

class ConversationalAgent:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
        self.model = AutoModelWithLMHead.from_pretrained("model")

    def question_model(self, question: str) -> str:
        bot_input_ids = self.tokenizer.encode(question + self.tokenizer.eos_token, return_tensors='pt')
        chat_history_ids = self.model.generate(
            bot_input_ids, max_length=100,
            pad_token_id=self.tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=10,
            top_p=0.3,
            temperature = 0.3
        )

        return self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
bot = ConversationalAgent()