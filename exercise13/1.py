from flask import Flask

app = Flask(__name__)
@app.route("/prime_number/<num>")
def prime_number(num):
    def primenumber(num):
        if num == 2 or num == 3:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
                    break
                elif i == (num-1):
                    return True
                    break

    response = {
        "Number": num,
        "isprime": primenumber(int(num))
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)