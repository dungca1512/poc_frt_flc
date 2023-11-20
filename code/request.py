import requests
import json

url = "https://cqe-dev-nlp.fpt.ai/dme/predict/dialogue/test"

payload = json.dumps({
  "project_info": {
    "callResultAI": {
      "task": "compare",
      "agent": {
        "cls_m3b_both": {
          "intents": {
            "nopay": "required",
            "paid": "required",
            "undefined": "required",
            "willpay": "required"
          },
          "entities": {},
          "threshold": 0.8,
          "version": "latest"
        }
      },
      "customer": {},
      "decision": [
        {
          "steps": [
            {
              "channel": "agent",
              "entities_logic": "or",
              "entities": [],
              "intent": "nopay",
              "lookup": {
                "n_lookup": None
              },
              "getFirst": True,
              "next_side": False,
              "except_entities": []
            }
          ],
          "title": "nopay",
          "approach": "top_down"
        },
        {
          "steps": [
            {
              "channel": "agent",
              "entities_logic": "or",
              "entities": [],
              "intent": "paid",
              "lookup": {
                "n_lookup": None
              },
              "getFirst": True,
              "next_side": False,
              "except_entities": []
            }
          ],
          "title": "paid",
          "approach": "top_down"
        },
        {
          "steps": [
            {
              "channel": "agent",
              "entities_logic": "or",
              "entities": [],
              "intent": "undefined",
              "lookup": {
                "n_lookup": None
              },
              "getFirst": True,
              "next_side": False,
              "except_entities": []
            }
          ],
          "title": "undefined",
          "approach": "top_down"
        },
        {
          "steps": [
            {
              "channel": "agent",
              "entities_logic": "or",
              "entities": [],
              "intent": "willpay",
              "lookup": {
                "n_lookup": None
              },
              "getFirst": True,
              "next_side": False,
              "except_entities": []
            }
          ],
          "title": "willpay",
          "approach": "top_down"
        }
      ],
      "start_turn": 0,
      "zone": [
        None,
        None
      ],
      "merge_turn": True,
      "default_decision": "no",
      "description": "[testing] summary call of willpay case",
      "version": "DEV"
    }
  },
  "transcript": [
    {
      "agent": True,
      "channel": 1,
      "start": 3.5,
      "end": 8.01,
      "text": "chào nhật gọi ra home credit việt nam đảm bảo đúng người phải trần thị thu phí đi"
    },
    {
      "channel": 2,
      "start": 9.190000000000001,
      "end": 9.68,
      "text": "đúng rồi"
    },
    {
      "agent": True,
      "channel": 1,
      "start": 11.82,
      "end": 16.6,
      "text": "ờ tôi biết tôi nhựt gọi ra home credit việt nam gọi tui báo về hợp đồng hồ sơ thẻ thúy trễ 8"
    },
    {
      "agent": True,
      "channel": 1,
      "start": 27.87,
      "end": 28.93,
      "text": "à đóng đi chị ơi"
    },
    {
      "channel": 2,
      "start": 29.88,
      "end": 30.580000000000002,
      "text": "alo alo"
    },
    {
      "agent": True,
      "channel": 1,
      "start": 31.14,
      "end": 32.620000000000005,
      "text": "ừ ngày nào đóng tiền tháng này thúy ơi"
    },
    {
      "channel": 2,
      "start": 34.19,
      "end": 35.699999999999996,
      "text": "ờ em đăng ký tiền anh ơi"
    },
    {
      "agent": True,
      "channel": 1,
      "start": 36.35,
      "end": 37.050000000000004,
      "text": "chừng nào đóng"
    },
    {
      "channel": 2,
      "start": 39.05,
      "end": 40.17,
      "text": "15 tây được không"
    },
    {
      "agent": True,
      "channel": 1,
      "start": 40.64,
      "end": 55.37,
      "text": "5 thì quá xa thế ơi hiểu khó khăn chưa tiền vay mượn tiền đóng sớm tránh kéo dài hồ sơ mình di chuyển địa phương nè nó bị xử lý để được xem xét mở thẻ tiếp tục dùng thẻ ưu đãi công ty chỉ hỗ trợ mình nay tới 12 tây đó là thứ 7 nay tới 12 tây ngày nào đóng 1600000"
    },
    {
      "agent": True,
      "channel": 1,
      "start": 62.019999999999996,
      "end": 62.42,
      "text": "biết rồi"
    },
    {
      "channel": 2,
      "start": 63.23,
      "end": 64.28999999999999,
      "text": "rồi để em tranh thủ"
    },
    {
      "agent": True,
      "channel": 1,
      "start": 64.64999999999999,
      "end": 66.36999999999999,
      "text": "hỗ trợ nay tới 12 tây ngày nào đóng được thúy"
    },
    {
      "channel": 2,
      "start": 69.42,
      "end": 73.27,
      "text": "thì cho hạn chốt 12 tây đi tại vì em nói 15 tây mới đóng được"
    },
    {
      "agent": True,
      "channel": 1,
      "start": 72.51,
      "end": 76.33,
      "text": "rất tiếc là 85000 đóng đủ triệu sáu trăm năm xong nợ trễ nha"
    },
    {
      "channel": 2,
      "start": 78.2,
      "end": 78.80999999999999,
      "text": "vâng vâng"
    },
    {
      "agent": True,
      "channel": 1,
      "start": 81.57,
      "end": 82.44999999999999,
      "text": "như cũ hay sao thế"
    },
    {
      "channel": 2,
      "start": 83.92,
      "end": 84.71,
      "text": "fpt á"
    },
    {
      "agent": True,
      "channel": 1,
      "start": 85.1,
      "end": 95.76,
      "text": "rồi ghi nhận cho mình đồng ý thanh toán 1685000 cho công ty ha chậm nhất 12 tây ngân hàng có sớm đóng sớm tránh kéo dài hồ sơ ghi nhận nợ xấu ảnh hưởng vay mượn tương lai trễ nhiều ngày bị nợ xấu ai giải quyết giùm ha xin chào"
    }
  ],
  "metadata": {},
  "criteria": [
    "callResultAI"
  ],
  "fileName": "1673405894624_3449_750908780518_499955608.mp3",
  "agentChannel": 1
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
