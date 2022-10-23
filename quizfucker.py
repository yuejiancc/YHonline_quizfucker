from bs4 import BeautifulSoup
import requests
import ddddocr

input_question = input("完整的输入问题： ")

# convert input_questions to raw_questions
def convert_question(input_question):
    raw_question = input_question.replace(" ", "")
    return raw_question

raw_question = convert_question(input_question)

print(raw_question)

# search the question on yhxt.liantibao.com

def get_answer_url(raw_question):
    url = "http://yhxt.liantibao.com/query.html?kw=" + raw_question
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    tag = str(soup.body.find_all(attrs={"class": "detail-list"}))
    handled_tag = tag.split("href=")[1].split("\"")[1]
    answer_url = "https://yhxt.liantibao.com" + handled_tag
    return answer_url

answer_url = get_answer_url(raw_question)

# get the answer
def get_answer(answer_url):
    url = answer_url
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    tag = str(soup.body.find_all(attrs={"class": "detail-answer"}))
    answer_pic_url = tag.split("src=")[1].split("\"")[1]

    ocr = ddddocr.DdddOcr()
    # pick up the answer using ddddocr
    with open("answer_pic.png", "wb+") as f:
        f.write(requests.get(answer_pic_url).content)

    img_bytes = open("answer_pic.png", "rb").read()
    answer = ocr.classification(img_bytes)

    return answer

answer = get_answer(answer_url).upper

print(answer)

# To be continued…