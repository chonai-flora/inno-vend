import requests
from datetime import datetime, timedelta, timezone


def send_line_notification(message):
    token = "XXXXXXXXXX"
    endpoint = "https://notify-api.line.me/api/notify"
    headers = { "Authorization": "Bearer " + token }
    params = { "message": message }
    response = requests.post(endpoint, headers=headers, data=params)
    http_status = response.status_code
    
    if http_status == 200:
        print("正常にトークルームに送信しました")
    else:
        print(f"トークルームに送信することができませんでした エラーコード: {http_status}")
        

def get_stock_messages():
    def format_count(count):
        if count > 0:
            return f"残り{count}個"
        return "終了しました"

    # サンプルデータ
    stocks = [
        {
            "name": "メロンパン",
            "count": 2
        },
        {
            "name": "野菜生活",
            "count": 2
        },
        {
            "name": "カップヌードル",
            "count": 0
        }
    ]

    stock_messages = []
    for stock in stocks:
        stock_message = f"{stock['name']}: {format_count(stock['count'])}"
        stock_messages.append(stock_message)

    return stock_messages

def main():
    now = datetime.now(timezone(timedelta(hours=+9), "JST"))
    stock_messages = get_stock_messages()
    formatted_stock_messages = "\n".join(stock_messages)
    message = (
        f"\n"
        f"{now:%-m月%-d日 %-H時%-M分}の在庫状況です\n\n"
        f"{formatted_stock_messages}"
    )
    
    send_line_notification(message)


if __name__ == "__main__":
    main()