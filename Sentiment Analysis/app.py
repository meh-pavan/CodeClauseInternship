from flask import Flask, render_template, request
from textblob import TextBlob

# Initialize Flask app
app = Flask(__name__)

# Function to perform sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        return "Positive Sentiment"
    elif sentiment < 0:
        return "Negative Sentiment"
    else:
        return "Neutral Sentiment"

# Route to display the input form
@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = ""
    
    if request.method == "POST":
        # Get the text from the form
        text = request.form["text"]
        
        # Perform sentiment analysis
        sentiment_result = analyze_sentiment(text)
    
    return render_template("index.html", sentiment_result=sentiment_result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
