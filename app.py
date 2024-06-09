import coc
import asyncio
from flask import Flask, render_template, request

app = Flask(__name__)

client = coc.Client()

# Đăng nhập không đồng bộ
async def login_async():
    await client.login(email="tadat216@gmail.com", password="zx1478956230")

# Hàm không đồng bộ để lấy dữ liệu người chơi
async def get_player_data(tag):
    await login_async()
    player_data = await client.get_player(tag)
    await client.close()
    return player_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_player', methods=['POST'])
def search_player():
    tag = request.form['tag']
    player_data = asyncio.run(get_player_data(tag))

    if player_data:
        return render_template('player.html', player_data=player_data)
    else:
        error_message = "Player not found or invalid tag."
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)