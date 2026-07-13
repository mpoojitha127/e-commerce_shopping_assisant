import pandas as pd

data = {
    "Question": [
        "What is an e-commerce website?",
        "How do I create an account?",
        "How do I log in?",
        "I forgot my password. What should I do?",
        "How do I search for a product?",
        "How do I filter products?",
        "Can I sort products?",
        "How do I add a product to my cart?",
        "How do I remove a product from my cart?",
        "How do I update product quantity in my cart?",
        "How do I place an order?",
        "Can I buy without an account?",
        "How do I apply a coupon code?",
        "Why is my coupon code not working?",
        "What payment methods are accepted?",
        "Can I pay using UPI?",
        "Is Cash on Delivery available?",
        "Is online payment secure?",
        "What should I do if my payment fails?",
        "Will I receive an order confirmation?",
        "How do I track my order?",
        "Where can I see my order history?",
        "Can I cancel my order?",
        "How do I cancel an order?",
        "Can I change my delivery address?",
        "How long does delivery take?",
        "Do you offer same-day delivery?",
        "What are the shipping charges?",
        "Do you provide free shipping?",
        "What if my order is delayed?",
        "How do I return a product?",
        "What is the return policy?",
        "Can I exchange a product?",
        "How long does a refund take?",
        "Where will my refund be credited?",
        "What if I receive a damaged product?",
        "What if I receive the wrong item?",
        "What should I do if an item is missing?",
        "Can I return an opened product?",
        "Which products are non-returnable?",
        "How do I contact customer support?",
        "Is live chat available?",
        "How do I file a complaint?",
        "How do I rate a product?",
        "Can I edit my review?",
        "Can I delete my review?",
        "How do I check product availability?",
        "What does 'Out of Stock' mean?",
        "Can I compare products?",
        "How do I add items to my wishlist?",
        "What is a wishlist?",
        "Can I share my wishlist?",
        "How do I update my profile?",
        "How do I change my password?",
        "Can I update my email address?",
        "Can I update my phone number?",
        "How do I delete my account?",
        "How do I subscribe to newsletters?",
        "How do I unsubscribe from emails?",
        "Do you offer gift cards?",
        "How do I redeem a gift card?",
        "What is EMI payment?",
        "Which banks support EMI?",
        "Do you offer student discounts?",
        "How do I check today's deals?",
        "What is a flash sale?",
        "How do I receive sale notifications?",
        "What are reward points?",
        "How do I redeem reward points?",
        "Do reward points expire?",
        "Can I download my invoice?",
        "Can I request a GST invoice?",
        "How do I report a fake product?",
        "Are all products authentic?",
        "What is a seller rating?",
        "How do I become a seller?",
        "Do you ship internationally?",
        "Can I schedule my delivery?",
        "What is contactless delivery?",
        "Can I reorder previous purchases?",
        "How do I find similar products?",
        "Can I buy multiple quantities?",
        "Is there a purchase limit?",
        "Can I preorder products?",
        "How do I enable app notifications?",
        "Can I shop using the mobile app?",
        "Is my personal information safe?",
        "Can I change the app language?",
        "How do I contact a seller?",
        "What is the estimated delivery date?",
        "How do I check product specifications?",
        "What does 'In Stock' mean?",
        "How do I report a website issue?",
        "Can I save my payment details?",
        "How do I use store credit?",
        "Can I combine coupons?",
        "How do I cancel a return request?",
        "Can I change my payment method after ordering?",
        "What happens if I miss my delivery?",
        "How do I check warranty information?",
        "Can I chat with customer support anytime?",
        "How can I get shopping assistance?"
    ],
    "Answer": [
        "An e-commerce website allows customers to buy and sell products online.",
        "Click Sign Up, enter your details, and verify your email.",
        "Use your registered email or phone number and password.",
        "Click 'Forgot Password' and follow the reset instructions.",
        "Use the search bar to find products.",
        "Use filters such as brand, price, rating, and category.",
        "Yes, you can sort by popularity, price, newest, or ratings.",
        "Click the 'Add to Cart' button.",
        "Go to your cart and click Remove.",
        "Use the quantity selector in your shopping cart.",
        "Proceed to checkout and complete the payment.",
        "Some stores allow guest checkout.",
        "Enter the coupon code during checkout.",
        "The coupon may be expired or not applicable.",
        "Credit cards, debit cards, UPI, wallets, net banking, and COD.",
        "Yes, UPI payments are supported.",
        "COD is available for eligible products and locations.",
        "Yes, secure encryption protects all online payments.",
        "Retry the payment or choose another payment option.",
        "Yes, you'll receive an email or SMS confirmation.",
        "Go to My Orders and click Track Order.",
        "Visit the My Orders section.",
        "Yes, before it is shipped.",
        "Go to My Orders and click Cancel.",
        "Yes, before dispatch.",
        "Usually between 2 and 7 business days.",
        "Available in selected cities.",
        "Shipping depends on your location and order value.",
        "Yes, on eligible orders.",
        "Track your order or contact support.",
        "Go to My Orders and select Return.",
        "Returns are accepted within the return window.",
        "Yes, if exchange is available.",
        "Usually within 5–7 business days.",
        "Refunds are sent to the original payment method.",
        "Request a replacement or refund immediately.",
        "Initiate a return request.",
        "Contact customer support.",
        "Depends on the product category.",
        "Customized and personal care items are usually non-returnable.",
        "Use chat, email, or phone support.",
        "Yes, during business hours.",
        "Submit a complaint through customer support.",
        "Go to your order and submit a rating.",
        "Yes, within the allowed period.",
        "Contact support if deletion is available.",
        "Availability is shown on the product page.",
        "The item is currently unavailable.",
        "Yes, using the Compare feature.",
        "Click the heart icon.",
        "A wishlist saves products for later.",
        "Some websites support wishlist sharing.",
        "Go to Account Settings.",
        "Change it in Security Settings.",
        "Yes, after verification.",
        "Yes, from your profile settings.",
        "Request account deletion in settings or contact support.",
        "Enable newsletters in account settings.",
        "Click the unsubscribe link in emails.",
        "Yes, digital gift cards are available.",
        "Enter the gift card code during checkout.",
        "EMI allows installment payments.",
        "Supported banks are listed during checkout.",
        "Occasionally during promotions.",
        "Visit the Deals page.",
        "A limited-time discount event.",
        "Enable app or email notifications.",
        "Points earned from purchases.",
        "Apply them during checkout.",
        "Yes, according to the program rules.",
        "Yes, from My Orders.",
        "Yes, provide GST details during checkout.",
        "Report it through customer support.",
        "Products are sourced from verified sellers.",
        "Seller ratings reflect customer feedback.",
        "Register through the seller portal.",
        "Yes, for selected products.",
        "Yes, if available for your location.",
        "Delivery without physical contact.",
        "Yes, from your order history.",
        "See the Recommended Products section.",
        "Yes, based on stock availability.",
        "Some products have quantity limits.",
        "Yes, for eligible products.",
        "Enable notifications in app settings.",
        "Yes, using the mobile application.",
        "Yes, your information is protected.",
        "Yes, in app settings.",
        "Use the seller contact option.",
        "The expected arrival date of your order.",
        "View the Specifications section.",
        "The product is available for purchase.",
        "Contact technical support.",
        "Yes, if secure payment storage is enabled.",
        "Apply available store credit during checkout.",
        "Usually only one coupon is allowed.",
        "Cancel it from the Returns section if eligible.",
        "Usually not after order confirmation.",
        "The courier may attempt delivery again.",
        "Warranty details are listed on the product page.",
        "Many stores provide 24/7 chat support.",
        "Use the AI shopping assistant or contact customer support."
    ]
}
df = pd.DataFrame(data)
print(df)
from datasets import load_dataset
df.to_json("train_data.json",orient="records",indent=4)
dataset=load_dataset("json",data_files="train_data.json")
print(dataset)
def formatting(data):
  return {
      "text":f"""### Question:{data["Question"]}
              ### Answer: {data["Answer"]}"""
  }
dataset=dataset["train"].map(formatting)
print(dataset)
tokenizer=AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token=tokenizer.eos_token
def tokenize(prompt):
  result=tokenizer(prompt["text"],
                   padding="max_length",
                   truncation=True,
                   max_length=128)
  result["labels"]=result["input_ids"].copy()
  return result
dataset=dataset.map(tokenize)
print(dataset)
import torch
from transformers import ( AutoTokenizer,AutoModelForCausalLM,
    Trainer,TrainingArguments,DataCollatorForLanguageModeling
)


model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


model = AutoModelForCausalLM.from_pretrained(
    model_name
)
from peft import(LoraConfig,get_peft_model)
config=LoraConfig(r=8,lora_alpha=16,
                  target_modules=["q_proj","v_proj"],
                  lora_dropout=0.1,bias="none",task_type="CAUSAL_LM")
model=get_peft_model(model,config)
model.print_trainable_parameters()
data_collator=DataCollatorForLanguageModeling(
    tokenizer=tokenizer,mlm=False
)
training_args=TrainingArguments(
    output_dir="./outputs",
    num_train_epochs=5,
    per_device_train_batch_size=1,
    learning_rate=2e-4,
    logging_steps=1,
    save_strategy="epoch",
    fp16=True
)
trainer=Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=data_collator
)
trainer.train()
model.save_pretrained("tinyllama_adapter")
tokenizer.save_pretrained("tinyllama_adapter")
device=next(model.parameters()).device
prompt="""### Question:
COD is available for eligible products and locations?


### Answer:
"""
inputs=tokenizer(prompt,return_tensors="pt")
inputs={k: v.to(device) for k,v in inputs.items()}
with torch.no_grad():
  output=model.generate(**inputs,max_new_tokens=100)
print(tokenizer.decode(output[0],skip_special_tokens=True))
