from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

def fibonacci(n):
    if n <= 0:
        return []

    sequence = [0, 1]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# Example usage
n = 1000

@app.route('/')
def hello():
    count = redis.incr('hits')

    result = fibonacci(n)

    return 'Hello World! I have been seen {} times. {} \n'.format(count, result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
