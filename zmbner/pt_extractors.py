from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

class NerExtractor:

    def __init__(self):
        # Initialize the model and tokenizer using a specified model.
        # The model used here is "pierreguillou/ner-bert-base-cased-pt-lenerbr", 
        # which is designed for Named Entity Recognition (NER) in Portuguese.
        model_name = "pierreguillou/ner-bert-base-cased-pt-lenerbr"
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def extract_entities(self, text):
        # Tokenize the input text. This involves breaking the text into words or symbols (tokens) 
        # that are meaningful for analysis.
        # 'max_length=512' ensures that the input is not longer than 512 tokens.
        # 'return_tensors="pt"' returns PyTorch tensors.
        inputs = self.tokenizer(text, max_length=512, truncation=True, return_tensors="pt")
        tokens = inputs.tokens()

        # Get model predictions. The model outputs logits, which are raw, unnormalized scores for each class.
        outputs = self.model(**inputs).logits
        predictions = torch.argmax(outputs, dim=2)

        # Process the model's predictions.
        entities_iob_format = []
        for token, prediction in zip(tokens, predictions[0].numpy()):
            # Map each token to its entity label (e.g., B-PER, I-LOC, O).
            entities_iob_format.append((token, self.model.config.id2label[prediction]))
        # Transform the entities from IOB format to a more readable format.
        return self._transform_entities(entities_iob_format)

    def _transform_entities(self, entities_iob_format):
            # Divide o texto em linhas individuais
            #linhas = texto.split('\n')
            # Lista para armazenar as entidades encontradas
            entidades = []
            # Variáveis para armazenar a entidade atual e seu rótulo
            entidade_atual = ''
            rotulo_atual = ''

            for i in range(1, len(entities_iob_format)-1):

                linha = entities_iob_format[i]
                # Avalia a string da linha para obter a tupla (palavra, rótulo)
                palavra, rotulo = linha

                if rotulo.startswith('B-'):
                    if not entidade_atual:
                        # Inicia uma nova entidade
                        entidade_atual = palavra
                        rotulo_atual = rotulo[2:]
                    else:
                        # Se 'B-' aparece mas já existe uma entidade sendo construída,
                        # verifica se o rótulo é o mesmo da entidade atual
                        if rotulo[2:] == rotulo_atual and palavra.startswith('##'):
                            # Continua a entidade atual (sem espaço, removendo '##')
                            entidade_atual += palavra[2:]
                        else:
                            if entidade_atual and not entidade_atual.startswith("##"):
                                # Finaliza a entidade atual e inicia uma nova
                                entidades.append((entidade_atual, rotulo_atual))
                            entidade_atual = palavra
                            rotulo_atual = rotulo[2:]

                elif rotulo.startswith('I-') and rotulo[2:] == rotulo_atual:
                    # Se a palavra for parte de uma entidade existente ('I-')
                    if palavra.startswith('##'):
                        # Anexa a palavra à entidade atual sem espaço, removendo '##'
                        entidade_atual += palavra[2:]
                    else:
                        # Anexa a palavra à entidade atual com um espaço
                        entidade_atual += ' ' + palavra

                elif rotulo == 'O':
                    # Finaliza a entidade atual quando encontrar um rótulo 'O'
                    if (entidade_atual and not entidade_atual.startswith("##")):
                        entidades.append((entidade_atual, rotulo_atual))
                        entidade_atual = ''
                        rotulo_atual = ''

            # Verifica se há uma entidade não adicionada após o loop
            if entidade_atual and not entidade_atual.startswith("##"):
                entidades.append((entidade_atual, rotulo_atual))

            return entidades