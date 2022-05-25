from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments

tokenizer = GPT2Tokenizer.from_pretrained('tokenizer')

tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

model = GPT2LMHeadModel.from_pretrained("GPyT").to("cpu")

while True:
    inp = input(">>> ")
    input_ids = tokenizer.encode(inp, return_tensors="pt").to("cpu")
    beam_output = model.generate(
        input_ids,
        max_length = 100,
        num_beams = 3,
        temperature = 0.7,
        no_repeat_ngram_size = 5,
        num_return_sequence = 3
    )

    for beam in beam_output:
        out = tokenizer.decode(beam)
        fout = out.replace("<N>", "\n")

        print(fout)