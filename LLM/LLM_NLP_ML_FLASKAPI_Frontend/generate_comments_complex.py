import pandas as pd
import random

# Helper function to generate random feedback
def generate_random_feedback(num_comments=1000):
    # More diverse and complex comments
    positive_comments = [
        "I love this product! It's amazing.",
        "Really happy with the purchase, highly recommend.",
        "Good value for money, I am satisfied.",
        "I had a wonderful time, everything was perfect.",
        "The product is decent, but the delivery was late.",
        "Exceptional quality, I’m so impressed.",
        "Totally worth the price. I would buy again!",
        "Perfect product, exceeded my expectations!",
        "I’m very happy with this, definitely worth it.",
        "The product works as described, no issues at all.",
        "The packaging was top-notch and the product works beautifully.",
        "Customer service was excellent, would buy again.",
        "This item changed my life, fantastic quality.",
        "It arrived earlier than expected and works great!",
        "Perfect for my needs, couldn’t be happier!"
    ]
    
    negative_comments = [
        "Worst experience ever, I hate it.",
        "It was a terrible experience, won't buy again.",
        "Horrible, I want a refund.",
        "The service was okay, could be better.",
        "Not bad, but not great either.",
        "Very disappointed. This was a complete waste of money.",
        "The product broke after one use. Terrible quality.",
        "I hate this, it’s completely useless to me.",
        "The customer service was awful, very unhelpful.",
        "It didn’t meet my expectations. I regret buying it.",
        "It was too complicated to use, not worth the hassle.",
        "Arrived damaged, wouldn’t recommend to anyone.",
        "The product was defective, I had to return it.",
        "It looks nothing like the picture, I'm disappointed.",
        "The shipping was delayed, and the product arrived broken."
    ]
    
    neutral_comments = [
        "The product works fine, nothing special.",
        "It met my expectations, but didn't exceed them.",
        "The service was average, neither good nor bad.",
        "The product is okay, but could use some improvements.",
        "It's a standard product, as expected.",
        "The item is acceptable, but not outstanding.",
        "It’s just okay, does what it’s supposed to do.",
        "I have no major complaints, but it’s nothing extraordinary.",
        "It works fine, but it could have been better for the price.",
        "It’s a decent product. Nothing too impressive though.",
        "Not the best I’ve used, but it gets the job done.",
        "Works as expected, but the design could be better.",
        "It’s functional, but I expected a bit more quality.",
        "The delivery was quick, but the product is just average.",
        "Okay product, but I don’t think I’ll buy again."
    ]
    
    # Diverse categories of feedback
    quality_comments = [
        "The product feels sturdy and well-built.",
        "The quality of the materials is amazing, feels premium.",
        "Not the best build quality, but it works.",
        "The quality of this item is below expectations, quite flimsy.",
        "I can tell this is built to last, excellent craftsmanship."
    ]
    
    service_comments = [
        "Customer service was prompt and helpful.",
        "It took a while to get a response, but they were polite.",
        "Had issues with the product, but customer service resolved it fast.",
        "Customer service wasn’t very responsive, which was frustrating.",
        "They resolved my issue quickly, great service."
    ]
    
    shipping_comments = [
        "The delivery was super fast, arrived ahead of schedule.",
        "The product arrived on time but was poorly packaged.",
        "Shipping was delayed, but they offered a discount for the trouble.",
        "The shipping process was smooth, no complaints.",
        "The package was damaged during shipping, very disappointing."
    ]
    
    comments = []
    for _ in range(num_comments):
        sentiment = random.choice(['positive', 'negative', 'neutral'])
        if sentiment == 'positive':
            comments.append(random.choice(positive_comments))
        elif sentiment == 'negative':
            comments.append(random.choice(negative_comments))
        else:
            comments.append(random.choice(neutral_comments))
        
        # Adding variety by mixing in other categories
        if random.random() < 0.2:  # 20% chance to add quality, service, or shipping feedback
            feedback_type = random.choice(['quality', 'service', 'shipping'])
            if feedback_type == 'quality':
                comments.append(random.choice(quality_comments))
            elif feedback_type == 'service':
                comments.append(random.choice(service_comments))
            else:
                comments.append(random.choice(shipping_comments))
    
    return comments

# Generate 1000 comments
data = {'feedback': generate_random_feedback(1000)}

# Create a DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("customer_feedback.csv", index=False)
print(f"Generated {len(df)} comments and saved to 'customer_feedback.csv'")
