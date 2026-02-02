# https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct/discussions/24
**URL:** https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct/discussions/24
**Page Title:** meta-llama/Meta-Llama-3-70B-Instruct · Anyone have used Llama 3 70B-I in huggingface Inference API ?
--------------------


## Anyone have used Llama 3 70B-I in huggingface Inference API ?

I thought they would not support as it is 70B, but looks they do as appear in the model page. Anyone have tried using it with api calls? If possible, I am trying to pay for PRO subscription
You can use it in poe.
I'm just testing it, but it doesn't seem to be working well.
- It looks like there is a max output token limit to ~250 which is very low
- I'm not sure if it correctly recognizes the format with roles - answers are weird
- I get duplicated response sometimes
- "return_full_text" = false doesn't work. I get in the response my initial prompt.
@ LJunius @ maxikq Thanks, I'll just try at my local with quantized model for now :(
It never returns a full response for me.
Does anyone know how to get a full response that is not truncated? Or can someone suggest a model that returns a full response?
· Sign up or log in to comment

--------------------