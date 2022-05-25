from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments

NEWLINECHAR = "<N>"

def encode_newlines(inp):
    return inp.replace("\n", NEWLINECHAR)

def decode_newlines(inp):
    return inp.replace(NEWLINECHAR, "\n")

tokenizer = GPT2Tokenizer.from_pretrained('GPyT_1/GPyT_TOK_75GB')

tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

model = GPT2LMHeadModel.from_pretrained("GPyT_1/latest_model").to("cpu")

inp = "def __init__"

input_ids = tokenizer.encode(inp, return_tensors="pt").to("cpu")
model_output = model.generate(
    input_ids,
    max_length = 100,
    num_beams = 3,
    temperature = 0.7,
    no_repeat_ngram_size = 5,
    num_return_sequence = 3,
    return_dict_in_generate = True,
    output_scores = True
)

for k in model_output:
    print(k)

for seq in model_output['sequences']:
    pass